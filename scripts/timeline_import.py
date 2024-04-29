"""
Input OA api and a list of people as targets, output 3 tables:
  - `paper`: tidy at paper level with PRIMARY KEY (`target/aid`, `doi`). We keep track of ego's status at that point in time, its age, position in the paper, ...
  - `coauthor`: tidy with PRIMARY KEY (`title(coauthor name/aid; name is weird because dataviz)`, `doi`). _Metadata is in relation to ego_. 
                Are they new acquaintance? Do they share institutions? 
                How many do they have collaborated with ego this year? Since the start of ego's career?
  - `author_info`: tidy at author-level with PRIMARY KEY (`aid`, `year`). For each year, we keep track of author's node metadata, e.g. 
                   institutions, citation count, author age, ... 

Running this script for ego/target is somehow costly in terms of API calls, and constrained by OpenAlex data schema,
so many decisions are made to account for both of these facts.
"""
import calendar
from collections import Counter
from datetime import datetime
from itertools import chain
import json
from pathlib import Path
from tqdm import tqdm
import random
import argparse
import pandas as pd
from pyalex import Works, Authors
import duckdb
import requests


def min_pub_year(target_aid, s2orc_id=None):
    """
    We find that OpenAlex often fails to get first author pub year right
    """
    # Authors for which we have manually verified their first year
    # It is important to get this right, as it determines age of target.
    # auth_known_first_yr = json.loads(open('./aid2firstyear.json', 'r').read())
    auth_known_first_yr = {
        "A5021345205": 2007,
        "A5037256938": 2004,
        "A5088506012": 1988,
        "A5017032627": 2000,
        "A5037170969": 1950,
        "A5027136376": 2005,
        "A5009266404": 2005,
        "A5046878011": 1987,
        "A5017357771": 2007,
        "A5040821463": 1999,
        "A5067142016": 1995,
        "A5012905268": 1997,
        "A5072481660": 1993,
        "A5085284243": 1989
    }
    if auth_known_first_yr.get(target_aid.upper()):
        return auth_known_first_yr[target_aid.upper()]
    else:
        return Works().filter(authorships={"author": {"id": target_aid}})\
                            .sort(publication_date="asc")\
                            .get()[0]['publication_year']
        
    # else:
        #!TODO: Find a way to have both oa and s2orc ID, without the ORCID. 
        # Probably via paper, which we have DOI, then fuzzy matching on names.
        # headers = {'x-api-key': '8mH99xWXoi60vMDfkSJtb6zVhSLiSgNP8ewg3nlZy'}
        # s2orc_id = 46280510
        # s2orc_url = f"https://api.semanticscholar.org/graph/v1/author/{s2orc_id}"
        # query_params = {'fields': 'externalIds,name,papers.year'}
        # response = requests.get(s2orc_url, params=query_params)
        # if response.status_code == 200:
        #     s2orc_papers = response.json()['papers']
        #     s2orc_min_year = min([x['year'] for x in s2orc_papers if x['year'] is not None])
        
        # return max((s2orc_min_year, oa_min_year))
        # pass
    
def most_recent_work(aid):
    return Works().filter(authorships={"author": {"id": aid}})\
                  .sort(publication_date="desc")\
                  .get()[0]

def max_pub_year(aid):
        return Authors()[aid]['counts_by_year'][0]['year']
    
def paper_db(con, aid=None):
    con.execute("""
        CREATE TABLE IF NOT EXISTS paper (
            type VARCHAR,
            target VARCHAR,
            aid VARCHAR,
            wid VARCHAR,
            pub_date DATE,
            pub_year INT,
            doi VARCHAR,
            title VARCHAR,
            author VARCHAR,
            author_age DATE,
            author_age_i INT,
            institution VARCHAR,
            cited_by_count INT,
            target_type VARCHAR,
            target_position VARCHAR,
            PRIMARY KEY(aid, wid)
        )
    """)

    if aid is not None:
        return (con.execute("SELECT aid, wid FROM paper WHERE aid = ?", (aid,)).fetchall())

def coauthor_db(con, name=None):
    con.execute("""
        CREATE TABLE IF NOT EXISTS coauthor (
            type VARCHAR,
            target VARCHAR,
            pub_date DATE,
            pub_year INT,
            author_age DATE,
            title VARCHAR,
            aid VARCHAR,
            acquaintance VARCHAR,
            yearly_collabo INT,
            all_times_collabo INT,
            shared_institutions VARCHAR,
            institution VARCHAR,
            target_type VARCHAR,
            PRIMARY KEY(target, title, pub_year)
        )
    """)
    
    if name is not None:
        return (con.execute("SELECT target, title, pub_year FROM coauthor WHERE target = ?", (name,)).fetchall())

def author_info_db(con):
    con.execute("""
        CREATE TABLE IF NOT EXISTS author_tidy (
            display_name VARCHAR,
            aid VARCHAR,
            pub_year INT,
            institution VARCHAR,
            first_pub_year INT,
            last_pub_year INT,
            author_age INT,
            PRIMARY KEY(aid, pub_year)
        )
    """) 

def shuffle_date_within_month(date_str):
    # Parse the date string to a datetime object
    date = datetime.strptime(date_str, "%Y-%m-%d")

    # Get the number of days in the month of the given date
    _, num_days_in_month = calendar.monthrange(date.year, date.month)

    # Generate a random day within the same month
    random_day = random.randint(1, num_days_in_month)

    # Create a new date with the randomly chosen day
    shuffled_date = date.replace(day=random_day)

    # Return the date in the desired format
    return shuffled_date.strftime("%Y-%m-%d")

def determine_home_inst(aid, works):
    # determine target home institution this year
    all_inst_this_year = []
    for w in works:
        for a in w['authorships']:
            if a['author']['id'].split("/")[-1] == aid:
                all_inst_this_year += [i['display_name'] for i in a['institutions']]
    return Counter(all_inst_this_year).most_common(1)[0][0] if len(all_inst_this_year) > 0 else None

def get_work_object_query(target_aid, yr):
    """returns to query to .get() or .paginate()"""
    return Works().filter(publication_year=yr, authorships={"author": { "id": target_aid }})

def get_pub_year_shuffled():
    pass

def range_db(con, aid):
    query_min = "SELECT pub_date FROM paper WHERE aid = ? ORDER BY pub_date DESC LIMIT 1"
    query_max = "SELECT pub_date FROM paper WHERE aid = ? ORDER BY pub_date ASC LIMIT 1"
    min_db = con.execute(query_min, (aid,)).fetchall()
    max_db = con.execute(query_max, (aid,)).fetchall()
    if len(min_db) > 0 and len(max_db) > 0:
        return min_db[0][0], max_db[0][0]

def is_db_up_to_date(con, target_aid, min_yr):
    """if in our DB we have the first year of the author and the last, we consider the DB updated."""
    min_max = range_db(con, target_aid)        
    max_oa =  datetime.strptime(most_recent_work(target_aid)['publication_date'], "%Y-%m-%d").date()
    min_oa = min_yr

    if min_max is None:
        return False
    else:
        return (min_oa >= min_max[1].year) and (max_oa < min_max[0])

def parse_args():
    parser = argparse.ArgumentParser("Data Downloader")
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        help="JSONlines file with urls and hashes",
        required=True,
    )
    parser.add_argument(
        "-o", "--output", type=Path, help="output directory", required=True
    )
    return parser.parse_args()

def main():
    
    args = parse_args()

    # load the input files
    assert args.input.exists(), "Input file does not exist"

    target_aids = pd.read_parquet(args.input)['OpenAlex id'].dropna().tolist()

    # load the DB
    con = duckdb.connect(str(args.output / "oa_data.db") )

    for target_aid in tqdm(target_aids, total=len(target_aids)):
        # target_aid='A5012905268'
        
        # Grab info about target author
        author_obj = Authors()[target_aid]
        target_name = author_obj['display_name']
        min_yr = min_pub_year(target_aid)
        max_yr = author_obj['counts_by_year'][0]['year']

        # Create cache DB if not exists, else return the cache
        cache_paper = paper_db(con, target_aid)
        cache_coauthor = coauthor_db(con, target_name)

        if is_db_up_to_date(con, target_aid, min_yr):
            print(f"{target_name} is up to date")
            continue
        
        print(f"Doing {target_name}")

        # Global values
        papers = []
        coauthors = []

        set_all_collabs = set()  # Set of all collaborators across time
        all_time_collabo = {}  # Dict(Name => (Collabo,)) across time
        set_collabs_of_collabs_never_worked_with = set() # useful to know when two authors know each other
        
        # Year -> targetName, will be useful.
        yr2age = { yr:i for i,yr in enumerate(range(min_yr, max_yr+1)) }

        for yr in yr2age.keys():
            
            # Yearly values to keep track
            dates_in_year = []  # List to keep track of dates for papers in this year
            all_target_inst_this_year = []
            new_collabs_this_year = set() 
            collabs_of_collabs_time_t = set() 
            coauthName2aid = {} # Dict(Name => OpenAlex ID) for the year
            time_collabo = {} # Dict(Name => (Collabo,)) for the year

            q = get_work_object_query(target_aid, yr)
            
            for w in chain(*q.paginate(per_page=200)):
                wid = w['id'].split("/")[-1]
                
                if w['type'] != 'article' and w['language'] != 'en':
                    continue

                # Add some noise within year for visualization purpose    
                shuffled_date = shuffle_date_within_month(w['publication_date'])
                # This is a hack to put different authors on the same yaxis.
                shuffled_auth_age = "1"+shuffled_date.replace(shuffled_date.split("-")[0], str(yr2age[yr]).zfill(3))
                # impossible leap year
                shuffled_auth_age = shuffled_auth_age.replace("29", "28") if shuffled_auth_age.endswith("29") else shuffled_auth_age
                dates_in_year.append(shuffled_date)

                # Now for each collaborator on that paper, check their institutions and collaboration count.
                for a in w['authorships']:
                    coauthor_name = a['author']['display_name']
                    
                    if coauthor_name != target_name:
                        institutions = a['institutions'] if 'institutions' in a else []
                        
                        # Increment collaboration count for the current year
                        author_yearly_data = time_collabo.get(coauthor_name, {'count': 0, 'institutions': {}})
                        author_yearly_data['count'] += 1
                        
                        # Increment institution count for the current year
                        for inst in institutions:
                            inst_name = inst['display_name']
                            author_yearly_data['institutions'][inst_name] = author_yearly_data['institutions'].get(inst_name, 0) + 1
                        
                        time_collabo[coauthor_name] = author_yearly_data
                        all_time_collabo[coauthor_name] = all_time_collabo.get(coauthor_name, 0) + 1

                        if coauthName2aid.get(coauthor_name) is None:
                            coauthor_aid = a['author']['id'].split("/")[-1]
                            coauthName2aid[coauthor_name] = coauthor_aid

                        # Add new collaborators to the set for all years
                        if coauthor_name not in set_all_collabs:
                            new_collabs_this_year.add(coauthor_name)

                    else: # if this is target, grab that information before moving on
                        all_target_inst_this_year += [i['display_name'] for i in a['institutions']]
                        target_position = a['author_position']
                        
                            
                # Majority vote to determine target_institution
                target_institution = Counter(all_target_inst_this_year).most_common(1)[0][0] if len(all_target_inst_this_year) > 0 else None
                
                if (target_aid, wid) not in cache_paper:
                    papers.append({
                        'type': 'paper',
                        'target': target_name,
                        'aid': target_aid,
                        'wid': wid,
                        'pub_date': shuffled_date,
                        'pub_year': int(w['publication_year']),
                        'doi': w['ids']['doi'] if 'doi' in w['ids'] else None,
                        'title': w['title'],
                        'author': ', '.join([_['author']['display_name'] for _ in w['authorships']]),
                        'author_age': shuffled_auth_age,
                        'author_age_i': yr2age[yr],
                        'institution': target_institution,
                        'cited_by_count': w['cited_by_count'],
                        'target_type': target_name + '-paper',
                        'target_position': target_position
                    })

            set_collabs_of_collabs_never_worked_with.update(
                    collabs_of_collabs_time_t - new_collabs_this_year - set_all_collabs - set([target_name])
                    )
            
            # At the end of each year, do yearly collaboration stats
            if len(time_collabo) > 0:            

                for coauthor_name, coauthor_data in time_collabo.items():
                    
                    if (target_name, coauthor_name, yr) in cache_coauthor:
                        continue

                    # Determine if it's a new or existing collaboration for the year
                    if coauthor_name in (new_collabs_this_year - set_all_collabs):
                        if coauthor_name in set_collabs_of_collabs_never_worked_with:
                            subtype = 'new_collab_of_collab'
                        else:
                            subtype = 'new_collab'
                    else:
                        subtype = 'existing_collab'

                    # Assign a date from the papers they collaborated on (if available)
                    author_date = random.choice(dates_in_year) if dates_in_year else str(yr)
                    shuffled_auth_age = "1"+author_date.replace(author_date.split("-")[0], str(yr2age[yr]).zfill(3))
                    # Impossible leap year
                    shuffled_auth_age = shuffled_auth_age.replace("29", "28") if shuffled_auth_age.endswith("29") else shuffled_auth_age

                    # Find whether coauthor shares institution with target
                    shared_inst = None
                    max_institution = None

                    if coauthor_data['institutions'] and target_institution:
                        max_institution = max(coauthor_data['institutions'], key=coauthor_data['institutions'].get)
                        if max_institution == target_institution:
                            shared_inst = max_institution

                    coauthors.append({
                        'type': 'coauthor',
                        'target': target_name,
                        'pub_date': author_date,  
                        'pub_year': int(author_date[0:4]),  # Use one of the dates from this year's papers
                        'author_age': shuffled_auth_age,
                        'title': coauthor_name,
                        'aid': coauthName2aid[coauthor_name],
                        'acquaintance': subtype,
                        'yearly_collabo': coauthor_data['count'],  
                        'all_times_collabo': all_time_collabo[coauthor_name],  
                        'shared_institutions': shared_inst,
                        'institution': max_institution,
                        'target_type': target_name+"-"+'coauthor'
                        })           


                set_all_collabs.update(new_collabs_this_year)


        # WRITE TO DATABASE --------------------------------------------
        
        # Function to preload publication year data from the database
        def preload_publication_years():
            query = "SELECT aid, first_pub_year, last_pub_year FROM author_tidy WHERE first_pub_year IS NOT NULL AND last_pub_year IS NOT NULL"
            results = con.execute(query).fetchall()
            for result in results:
                aid, min_year, max_year = result
                publication_year_cache[aid] = (min_year, max_year)


        # Function to get min and max publication years, with caching and API fallback
        def get_publication_years(aid):
            if aid not in publication_year_cache:
                min_year = min_pub_year(aid)  # API call assumed
                max_year = max_pub_year(aid)  # API call assumed
                publication_year_cache[aid] = (min_year, max_year)
            return publication_year_cache[aid]


        # TABLE 1: PAPER
        
        if len(papers) > 0:   
            con.executemany( """
                    INSERT INTO paper
                    (type, target, aid, wid, pub_date, pub_year, doi, title, author, author_age, author_age_i, institution, cited_by_count, target_type, target_position)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, [list(_.values()) for _ in papers])

        # TABLE 2 COAUTHORS
       
        if len(coauthors) > 0:        
            con.executemany( """
                    INSERT INTO coauthor
                    (type, target, pub_date, pub_year, author_age, title, aid, acquaintance, yearly_collabo, all_times_collabo, shared_institutions, institution, target_type)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, )
            """, [list(_.values()) for _ in coauthors])

        # TABLE 3:AUTHOR INFO
        
        if len(papers) > 0 and len(coauthors) > 0:
            dedup_author_df = pd.concat([
                pd.DataFrame(papers)[['target', 'aid', 'pub_year', 'institution']], 
                pd.DataFrame(coauthors).loc[:,['title', 'aid', 'pub_year', 'institution']]\
                                       .rename(columns={'title': 'target'})], 
            axis=0).drop_duplicates()
            
            # Cache for storing publication years
            publication_year_cache = {}
            preload_publication_years()

            data_batch = []
            for _, group in tqdm(dedup_author_df.groupby('aid')):
                for _, row in group.iterrows():
                    display_name, aid, pub_year, inst = row['target'], row['aid'], int(row['pub_year']), row['institution']

                    try:
                        # costly bit right now; we need to call twice the API to get min, max for each target coauthors
                        # since we are caching the results, this will get faster overtime.
                        min_year, max_year = get_publication_years(aid)
                        author_age = pub_year - min_year
                        data_batch.append((display_name, aid, pub_year, inst, min_year, max_year, author_age))
                    except: # very rarely it fails, just ignore it
                        print(f"{display_name} failed to have range of year")
                        pass

            query = """
                INSERT INTO author_tidy
                (display_name, aid, pub_year, institution, first_pub_year, last_pub_year, author_age)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT (aid, pub_year) DO UPDATE SET
                display_name = EXCLUDED.display_name,
                institution = EXCLUDED.institution,
                first_pub_year = EXCLUDED.first_pub_year,
                last_pub_year = EXCLUDED.last_pub_year,
                author_age = EXCLUDED.author_age
            """
            con.executemany(query, data_batch)
        

    # Commit and close DB connection
    con.commit()
    con.close()


    # Manually fixing some first publication year values
    # con = duckdb.connect("../docs/data/oa_data.db")

    # def replace_new_min_year(con, aid, name, new_min_year):
        
    #     con.sql(f"UPDATE author_tidy SET first_pub_year={new_min_year} WHERE aid = '{aid}'")
        
    #     con.sql(f"DELETE FROM author_tidy WHERE aid = '{aid}' AND pub_year < {new_min_year}")
    #     con.sql(f"DELETE FROM author_tidy WHERE display_name = '{name}' AND pub_year < {new_min_year}")
        
    #     con.sql(f"DELETE FROM paper WHERE aid = '{aid}' AND pub_year < {new_min_year}")
    #     con.sql(f"DELETE FROM paper WHERE target = '{name}' AND pub_year < {new_min_year}")
        
    #     con.sql(f"DELETE FROM coauthor WHERE aid = '{aid}' AND pub_year < {new_min_year} ")
    #     con.sql(f"DELETE FROM coauthor WHERE target = '{name}' AND pub_year < {new_min_year}")
        
    #     # update age
    #     con.sql(f"UPDATE author_tidy SET author_age = pub_year-first_pub_year WHERE aid = '{aid}'")
        
    #     con.sql("")
    #     # con.sql(f"UPDATE paper SET author_age = pub_year-first_pub_year WHERE display_name = '{name}'")
        
    #     con.commit()
    
    # replace_new_min_year(con, "A5021345205", "F. Guillaume Blanchet", 2007)
    # replace_new_min_year(con, "a5021345205", "F. Guillaume Blanchet", 2007)
    # replace_new_min_year(con, "A5067142016", "M. E. J. Newman", 1995)
    # replace_new_min_year(con, "A5012905268", "Réka Albert", 1997)

    # delete lwoer case
    # con.sql("DELETE FROM author_tidy WHERE aid = 'a5012905268'")
    # con.commit()

    # def clean_db_from(con, aid, name):

    #     con.execute("DELETE FROM paper WHERE aid = ?", (aid,))
    #     con.execute("DELETE FROM paper WHERE target = ?", (name,))
        
    #     # In coauthor table it, we just get rid of the target rows
    #     # We don't want to remove that persons from the coauthorship of others.
    #     con.execute("DELETE FROM coauthor WHERE target = ?", (name,))
        
    #     # In author_tidy, we remove all all rows for that person
    #     con.execute("DELETE FROM author_tidy WHERE aid = ?", (aid,))
    #     con.execute("DELETE FROM author_tidy WHERE display_name = ?", (name,))
        
    #     con.commit()

    # clean_db_from(con, 'A5000679279', 'Duncan J. Watts')
    # clean_db_from(con, 'A5012905268', 'Réka Albert')
            
    # con.close()



if __name__ == "__main__":

    main()