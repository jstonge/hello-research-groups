#!/usr/bin/env python3
import dotenv
dotenv.load_dotenv()

import requests
import json
import os
import re
import wget
from tqdm import tqdm

S2_API_KEY = os.environ['S2_API_KEY']

#  SEARCH API BASED ON ELASTIC SEARCH

url = 'https://api.semanticscholar.org/graph/v1/paper/search'

# Define the required query parameter and its value (in this case, the keyword we want to search for)
query_params = {
    'query': 'religion',
    'limit': 5,
    'publicationTypes': 'JournalArticle',
    'year': '2010',
    'fields': 'title,publicationTypes,publicationDate,isOpenAccess,openAccessPdf,embedding.specter_v2',
    'fieldsOfStudy': 'Sociology'
}

# Define a separate function to make a request to the paper details endpoint using a paper_id. This function will be used later on (after we call the paper search endpoint).
def get_paper_data(paper_id):
  url = 'https://api.semanticscholar.org/graph/v1/paper/' + paper_id

  # Define which details about the paper you would like to receive in the response
  paper_data_query_params = {'fields': 'title,year,abstract,authors.name,'}

  # Send the API request and store the response in a variable
  response = requests.get(url, params=paper_data_query_params)
  if response.status_code == 200:
    return response.json()
  else:
    return None

# Make the GET request to the paper search endpoint with the URL and query parameters
headers = {'x-api-key': S2_API_KEY}
search_response = requests.get(url, params=query_params, headers=headers)

# Check if the request was successful (status code 200)
if search_response.status_code == 200:
    search_response = search_response.json()

    # Retrieve the paper id corresponding to the 1st result in the list
    paper_id = search_response['data'][0]['paperId']

    # Retrieve the paper details corresponding to this paper id using the function we defined earlier.
    paper_details = get_paper_data(paper_id)

    # Check if paper_details is not None before proceeding
    if paper_details is not None:
        pass
    # Your code to work with the paper details goes here
    else:
        print("Failed to retrieve paper details.")


# BULK DOWNLOAD BASED ON FIELD OF STUDY``

# modify these
DATASET_NAME = "s2orc"
LOCAL_PATH = "../../data/raw/s2orc"
os.makedirs(LOCAL_PATH, exist_ok=True)
# get latest release's ID
response = requests.get("https://api.semanticscholar.org/datasets/v1/release/latest").json()
RELEASE_ID = response["release_id"]
print(f"Latest release ID: {RELEASE_ID}")


query_params = {
    'limit': 5,
    'publicationTypes': 'JournalArticle',
    'year': '2010',
    'fields': 'title,publicationTypes,venue,journal,publicationDate,isOpenAccess,s2FieldsOfStudy,openAccessPdf',
    'fieldsOfStudy': 'Sociology'
}

url = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
headers = {'x-api-key': S2_API_KEY}
bulk_response = requests.get(url, params=query_params, headers=headers)

bulk_response = bulk_response.json()

url="https://images.webofknowledge.com/images/help/WOS/hp_research_areas_easca.html"
p=requests.get(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(p.content, 'html.parser')
table=soup.find('table')
# BULK DOWNLOAD THE WHOLE DB

# get the download links for the s2orc dataset; needs to pass API key through `x-api-key` header
# download via wget. this can take a while...
response = requests.get(f"https://api.semanticscholar.org/datasets/v1/release/{RELEASE_ID}/dataset/{DATASET_NAME}/", headers={"x-api-key": S2_API_KEY}).json()
for url in tqdm(response["files"]):
    # break
    match = re.match(r"https://ai2-s2ag.s3.amazonaws.com/staging/(.*)/s2orc/(.*).gz(.*)", url)
    assert match.group(1) == RELEASE_ID
    SHARD_ID = match.group(2)
    wget.download(url, out=os.path.join(LOCAL_PATH, f"{SHARD_ID}.gz"))
print("Downloaded all shards.")