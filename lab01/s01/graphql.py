import os
import csv
import requests
from dotenv import load_dotenv

load_dotenv()

endpoint = "https://api.github.com/graphql"
headers = {'Authorization': f'Bearer {os.getenv("ACCESS_TOKEN")}'}

def run_query(query, csv_filename):

  all_repositories = []
  after_cursor = None
  remaining_results = 1000

  while results_remaning > 0:
    variables = {
      "queryString": "stars :> 1000",
      "first": min (50, results_remaning),
      "after": after_cursor
    }

    request = requests.post(endpoint, json={'query': query, "variables": variables}, headers=headers)
 
    edges = response_data["data"]["search"]["edges"]
    all_repositories.extend(edges)
    remaining_results -= len(edges)

    page_info = response_data["data"]["search"]["pageInfo"]
    has_next_page = page_info["hasNextPage"]
    after_cursor = page_info["endCursor"]

    if not has_next_page:
      break

  if request.status_code == 200:
    return show_results(request.json(), csv_filename)
  else:
    raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
  

def show_results(results):
  response = results["data"]["search"]["nodes"]

  with open(csv_filename, "lab_2", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Repository", "Métric"])  # Colunas do CSV

  for item in response:
    repo_name = item["name"]
    metric_value = item["stargazerCount"]  # Substituir pela métrica correta
    csv_writer.writerow([repo_name, metric_value])

  print(response)