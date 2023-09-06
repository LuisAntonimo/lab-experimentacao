import os
import csv
from datetime import datetime
import requests
from dotenv import load_dotenv
import plot

load_dotenv()

endpoint = "https://api.github.com/graphql"
headers = {'Authorization': f'Bearer {os.getenv("ACCESS_TOKEN")}'}

def run_query(query, csv_filename, metrics):

  with open(csv_filename + '.csv', "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(metrics)

    data = []
    plot_data = []

    after_cursor = None
  
    for i in range(10):
      variables = {
        "after": after_cursor,
      }

      request = requests.post(endpoint, json={'query': query, "variables": variables}, headers=headers)
  

      if request.status_code == 200:
        response = request.json()

        repositories = response['data']['search']['edges']

        for item in repositories:
          node = item["node"]
          repo_name = node["name"]
          stars = node["stargazerCount"]


          # creation_date = node['createdAt']
          last_update = node['updatedAt']
          # pulls = node['pullRequests']['totalCount']
          # releases = node['releases']['totalCount']
          # languages = node['languages']['edges']
          # total_issues = node['total_issues']['totalCount']
          # closed_issues = node['closed_issues']['totalCount']
          
          data += [repo_name, stars, get_days(last_update)]

          # if bool(languages):
          #   data += [repo_name, stars, languages[0]['node']['name']]
          # else:
          #   data += [repo_name, stars]

          csv_writer.writerow(data)
          
          # plot_data.append(plot.get_age(creation_date))

          data = []
        
        

        after_cursor = response['data']['search']['pageInfo']['endCursor']


      else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
      # plot.make(plot_data)
    
def get_days(last_update):
  date_now = datetime.now()
  update_date = datetime.strptime(last_update, "%Y-%m-%dT%H:%M:%SZ")
  age = date_now - update_date

  return age.seconds

def get_issues(total, closed):
  if (total == 0):
    issues = 0
  else:
    issues = (closed/total)

  return f'{issues:.2f}'