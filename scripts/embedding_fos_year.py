#!/usr/bin/env python3
import dotenv
dotenv.load_dotenv()

import requests
import umap
import os
import duckdb
from time import sleep



def embedding_db(con):
    con.execute("""
        CREATE TABLE IF NOT EXISTS embeddings (
            fos VARCHAR,
            year INTEGER,
            title VARCHAR,
            venue VARCHAR,
            url VARCHAR,
            abstract VARCHAR,
            publicationDate DATE,
            publicationTypes VARCHAR,
            citationCount INTEGER,
            authors VARCHAR,
            external_fos VARCHAR,
            x VARCHAR,
            y VARCHAR,
        )
    """) 
    
def embedding_db_meta(con):
    con.execute("""
        CREATE TABLE IF NOT EXISTS lookup (
                fos VARCHAR,
                year INTEGER,
                PRIMARY KEY (fos, year)
                );
    """) 

def main():
    con = duckdb.connect('embeddings.db')
    S2_API_KEY = os.environ['S2_API_KEY']
    FoS = 'History'
    YEAR = 2020
    headers = {'x-api-key': S2_API_KEY}
    meta = []
    embeddings = []

    NB_BATCH = 3
    i=0
    query_params = {
            'publicationTypes': 'JournalArticle',
            'year': YEAR,
            'minCitationCount': 3,
            'fields': 's2FieldsOfStudy', 
            'fieldsOfStudy': FoS
    }

    while i < NB_BATCH:   
        # get the list of papers based on s2fos using bulk query
        bulk_response = requests.get(
            "https://api.semanticscholar.org/graph/v1/paper/search/bulk", 
            params=query_params, 
            headers=headers
        )
        
        if bulk_response.status_code != 200:
            print(f"Didn't work : {bulk_response.text}")
            # break

        bulk_response = bulk_response.json()
        sleep(1)

        list_paper_ids = [_['paperId'] for _ in bulk_response['data']]
        batchsize=500
        nb_papers=len(list_paper_ids)
        
        for j in range(0, nb_papers, batchsize):
            batch_papers = list_paper_ids[j:j+batchsize]
            
            # get the details of the papers using paper/batch
            r = requests.post(
                'https://api.semanticscholar.org/graph/v1/paper/batch',
                params={'fields': 'title,publicationTypes,authors.name,venue,url,s2FieldsOfStudy,abstract,publicationDate,isOpenAccess,openAccessPdf,embedding.specter_v2,citationCount,referenceCount'},
                json={"ids": batch_papers}
            )
            
            if r.status_code == 200:
                paper_details = r.json()
                paper_details = [p for p in paper_details if p.get('embedding') and p['embedding'].get('vector')]
                embeddings += [p['embedding']['vector'] for p in paper_details]

                meta += [
                    [
                        FoS, YEAR, p['title'], p['abstract'], p['venue'], p['url'],
                        p['publicationDate'], p['publicationTypes'][0], p['citationCount'], 
                        ', '.join([_['name'] for _ in p['authors']]),
                        ', '.join([f"{_['category']}/{_['source']}" for _ in p['s2FieldsOfStudy']])
                    ]
                    for p in paper_details
                    ]
            else:
                print(f"Didn't work : {r.text}")
                # break
            
        nexttoken = bulk_response['token']
        if nexttoken is not None:
            query_params['token'] = nexttoken
        else:
            query_params.pop('token', None)
        i += 1
        sleep(1)
        
    reducer = umap.UMAP()
    embedding2d = reducer.fit_transform(embeddings)
    
    meta = [a+b.tolist() for a,b in zip(meta, embedding2d)]
        
    con.execute("INSERT INTO lookup (fos, year) VALUES (?, ?)", (FoS, YEAR,))
     
    con.executemany("""
            INSERT INTO embeddings 
            (fos, year, title, abstract, venue, url, publicationDate, publicationTypes, citationCount, authors, external_fos, x, y) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", meta)
    

    con.commit()
    con.close()

if __name__ == '__main__':
    main()