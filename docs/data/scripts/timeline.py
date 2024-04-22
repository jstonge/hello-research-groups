"""
Input OA api and a list of people as target, output 3 tables:
  - `paper`: tidy at paper level with PRIMARY KEY (`target/aid`, `doi`). We keep track of ego's status at that point in time, its age, position in the paper, ...
  - `coauthor`: tidy with PRIMARY KEY (`title(coauthor name/aid; name is weird because dataviz)`, `doi`). _Metadata is in relation to ego_. 
                Are they new acquaintance? Do they share institutions? 
                How many do they have collaborated with ego this year? Since the start of ego's career?
  - `author_info`: tidy at author-level with PRIMARY KEY (`aid`, `year`). For each year, we keep track of author's node metadata, e.g. 
                   institutions, citation count, author age, ... 

Running this script for ego/target is somehow costly in terms of API calls, and constrained by OpenAlex data schema,
so many decisions are made to account for both of these facts.
"""
from pyalex import Works, Authors
from itertools import chain
from tqdm import tqdm
from time import sleep
import argparse
from pathlib import Path
import pandas as pd
from datetime import datetime
import calendar
import random
from collections import Counter
import duckdb

from helpers import get_all_work_time_t, find_all_colabs, write_jsonl

def min_pub_year(target_aid):
    return Works().filter(authorships={"author": {"id": target_aid}})\
                        .sort(publication_date="asc")\
                        .get()[0]['publication_year']
    
def max_pub_year(aid):
    try:
        return Works().filter(authorships={"author": {"id": aid}})\
                    .sort(publication_date="desc")\
                    .get()[0]['publication_year']
    except:
        return Authors()[aid]['counts_by_year'][0]['year']
    
def create_paper_db(con):
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

def create_coauthor_db(con):
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

def create_author_info_db(con):
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


def main():

    target_aids=pd.read_csv("../researchers.tsv", delimiter="\t", usecols=['OpenAlex id (optional)']).dropna(subset=['OpenAlex id (optional)']).iloc[:,0].tolist()

    auth_known_first_yr = {}
    
    # authors for which we verified manually their first year
    auth_known_first_yr['A5037256938'] = 2004
    auth_known_first_yr['A5088506012'] = 1988
    auth_known_first_yr['A5017032627'] = 2000
    auth_known_first_yr['A5037170969'] = 1950
    auth_known_first_yr['A5027136376'] = 2005
    auth_known_first_yr['A5009266404'] = 2005
    auth_known_first_yr['A5046878011'] = 1987
    auth_known_first_yr['A5017357771'] = 2007
    auth_known_first_yr['A5040821463'] = 1999

    for target_aid in target_aids:
        # target_aid = 'a5040821463'
        papers = []
        coauthors = []

        set_all_collabs = set()  # Track all collaborators across all years
        set_collabs_of_collabs_never_worked_with = set()
        all_time_collabo = {}  # Reset for each year
        
        target_name = Authors()[target_aid]['display_name']
        min_yr = auth_known_first_yr[target_aid.upper()] if auth_known_first_yr.get(target_aid.upper()) else min_pub_year(target_aid)
        max_yr = max_pub_year(target_aid)
        yr2age = { yr:i for i,yr in enumerate(range(min_yr, max_yr+1)) }
        

        for yr in range(min_yr, max_yr+1):
            # yr = min_yr
            
            time_collabo = {}  # Reset for each year
            dates_in_year = []  # List to keep track of dates for papers in this year
            new_collabs_this_year = set() 
            all_target_inst_this_year = []
            coauthName2aid = {}

            collabs_of_collabs_time_t = set()

            # Not doing the collab of collab stuff makes it much cheaper; we put it aside for now.
            # But this means that the triadic closure thing is wrong rn.
            # collab of collabs
            # target_collaborators_time_t = find_all_colabs(target_aid, dat[yr])
            # collabs_of_collabs_time_t = get_collabs_of_collabs_time_t(target_collaborators_time_t, yr, names=True)

            q = get_work_object_query(target_aid, yr)
            
            for record in chain(*q.paginate(per_page=200)):
                
                if record['type'] != 'article' and record['language'] != 'en':
                    continue
                        
                shuffled_date = shuffle_date_within_month(record['publication_date'])
                shuffled_auth_age = "1"+shuffled_date.replace(shuffled_date.split("-")[0], str(yr2age[yr]).zfill(3))
                shuffled_auth_age = shuffled_auth_age.replace("29", "28") if shuffled_auth_age.endswith("29") else shuffled_auth_age
                dates_in_year.append(shuffled_date)

                for a in record['authorships']:
                    coauthor_name = a['author']['display_name']
                    
                    if coauthor_name == target_name:
                        all_target_inst_this_year += [i['display_name'] for i in a['institutions']]
                        target_position = a['author_position']

                    else:
                        
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
                            
                # majority vote to determine target_institutio
                target_institution = Counter(all_target_inst_this_year).most_common(1)[0][0] if len(all_target_inst_this_year) > 0 else None
                
                papers.append({
                    'type': 'paper',
                    'target': target_name,
                    'aid': target_aid,
                    'wid': record['id'].split("/")[-1],
                    'pub_date': shuffled_date,  # Ensure this is a string in 'YYYY-MM-DD' format
                    'pub_year': int(record['publication_year']),
                    'doi': record['ids']['doi'] if 'doi' in record['ids'] else None,
                    'title': record['title'],
                    'author': ', '.join([_['author']['display_name'] for _ in record['authorships']]),
                    'author_age': shuffled_auth_age,
                    'author_age_i': yr2age[yr],
                    'institution': target_institution,
                    'cited_by_count': record['cited_by_count'],
                    'target_type': target_name + '-paper',
                    'target_position': target_position
                })

            set_collabs_of_collabs_never_worked_with.update(
                    collabs_of_collabs_time_t - new_collabs_this_year - set_all_collabs - set([target_name])
                    )
            
            # At the end of each year, do yearly collaboration stats

            if len(time_collabo) > 0:            

                for author_name, author_data in time_collabo.items():

                    # Determine if it's a new or existing collaboration for the year
                    if author_name in (new_collabs_this_year - set_all_collabs):
                        if author_name in set_collabs_of_collabs_never_worked_with:
                            subtype = 'new_collab_of_collab'
                        else:
                            subtype = 'new_collab'
                    else:
                        subtype = 'existing_collab'

                    # Assign a date from the papers they collaborated on (if available)
                    author_date = random.choice(dates_in_year) if dates_in_year else str(yr)
                    shuffled_auth_age = "1"+author_date.replace(author_date.split("-")[0], str(yr2age[yr]).zfill(3))
                    # impossible leap year
                    shuffled_auth_age = shuffled_auth_age.replace("29", "28") if shuffled_auth_age.endswith("29") else shuffled_auth_age

                    # find coauthor institution name
                    shared_inst = None
                    max_institution = None
                    
                    if author_data['institutions'] and target_institution:
                        max_institution = max(author_data['institutions'], key=author_data['institutions'].get)
                        if max_institution == target_institution:
                            shared_inst = max_institution

                    coauthors.append({
                        'type': 'coauthor',
                        'target': target_name,
                        'pub_date': author_date,  # Use one of the dates from this year's papers
                        'pub_year': int(author_date[0:4]),  # Use one of the dates from this year's papers
                        'author_age': shuffled_auth_age,
                        'title': author_name,
                        'aid': coauthName2aid[author_name],
                        'acquaintance': subtype,
                        'yearly_collabo': author_data['count'],  # Total collaboration count for the year
                        'all_times_collabo': all_time_collabo[author_name],  # Total collaboration count
                        'shared_institutions': shared_inst,
                        'institution': max_institution,
                        'target_type': target_name+"-"+'coauthor'
                        })                  

                set_all_collabs.update(new_collabs_this_year)


        # CREATE DATABASE
        


        con = duckdb.connect("../oa_data.db")


        # TABLE 1

        
        create_paper_db(con)
        
        con.executemany( """
                INSERT INTO paper
                (type, target, aid, wid, pub_date, pub_year, doi, title, author, author_age, author_age_i, institution, cited_by_count, target_type, target_position)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, [list(_.values()) for _ in papers])


        # TABLE 2

        create_coauthor_db(con)
        
        con.executemany( """
                INSERT INTO coauthor
                (type, target, pub_date, pub_year, author_age, title, aid, acquaintance, yearly_collabo, all_times_collabo, shared_institutions, institution, target_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, )
        """, [list(_.values()) for _ in coauthors])


        # TABLE 3: (Update) AUTHOR INFO


        create_author_info_db(con)
        
        dedup_author_df = pd.concat([
            pd.DataFrame(papers)[['target', 'aid', 'pub_year', 'institution']], 
            pd.DataFrame(coauthors)[['title', 'aid', 'pub_year', 'institution']].rename(columns={'title': 'target'})], 
        axis=0).drop_duplicates()
        

        # Function to preload publication year data from the database
        def preload_publication_years():
            query = "SELECT aid, first_pub_year, last_pub_year FROM author_tidy WHERE first_pub_year IS NOT NULL AND last_pub_year IS NOT NULL"
            results = con.execute(query).fetchall()
            for result in results:
                aid, min_year, max_year = result
                publication_year_cache[aid] = (min_year, max_year)

        # Function to perform bulk insert
        def bulk_insert(data):
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
            con.executemany(query, data)

        # Function to get min and max publication years, with caching and API fallback
        def get_publication_years(aid):
            if aid not in publication_year_cache:
                min_year = min_pub_year(aid)  # API call assumed
                max_year = max_pub_year(aid)  # API call assumed
                publication_year_cache[aid] = (min_year, max_year)
            return publication_year_cache[aid]

        # Cache for storing publication years
        publication_year_cache = {}
        # Preload the cache
        preload_publication_years()

        data_batch = []
        for author, group in tqdm(dedup_author_df.groupby('aid')):
            for i, row in group.iterrows():
                display_name, aid, pub_year, inst = row['target'], row['aid'], int(row['pub_year']), row['institution']
                min_year, max_year = get_publication_years(aid)
                author_age = pub_year - min_year
                data_batch.append((display_name, aid, pub_year, inst, min_year, max_year, author_age))


        bulk_insert(data_batch)
        
        con.commit()

        con.close()


        # Manually fixing some first publication year values

        # con.sql("DESCRIBE TABLE paper")
        # con.sql("DESCRIBE TABLE coauthor")
        # con.sql("DESCRIBE TABLE author_tidy")

        # def replace_new_min_year(con, aid, new_min_year):
        #     # update first_pub_year
        #     con.sql(f"UPDATE author_tidy SET first_pub_year={new_min_year} WHERE aid = '{aid}'")
        #     con.sql(f"DELETE FROM paper WHERE aid = '{aid}' AND pub_year < {new_min_year}")
        #     con.sql(f"DELETE FROM coauthor WHERE target = '{aid}' AND pub_year < {new_min_year} ")
        #     con.sql(f"DELETE FROM author_tidy WHERE aid = '{aid}' AND pub_year < {new_min_year}")
            
        #     # update age
        #     con.sql(f"UPDATE author_tidy SET author_age = pub_year-first_pub_year WHERE aid = '{aid}'")
            
        #     con.commit()
        
        # replace_new_min_year(con, target_aid, min_yr)
                
        # con.close()



if __name__ == "__main__":
    main()