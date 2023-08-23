import os
import requests
from dotenv import load_dotenv

load_dotenv()

endpoint = "https://api.github.com/graphql"
headers = {'Authorization': f'Bearer {os.getenv("ACCESS_TOKEN")}'}

def run_query(query):
  request = requests.post(endpoint, json={'query': query}, headers=headers)
  if request.status_code == 200:
    return show_results(request.json())
  else:
    raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
  

def show_results(results):
  response = results["data"]["search"]["nodes"]
  print(response)