import os
import requests
from dotenv import load_dotenv

load_dotenv()

endpoint = "https://api.github.com/graphql"

headers = {'Authorization': f'Bearer {os.getenv("ACCESS_TOKEN")}'}


def run(query):
  request = requests.post(endpoint, json={'query': query}, headers=headers)
  if request.status_code == 200:
    return request.json()
  else:
    raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

rq01_query = """
  {
    search(query: "stars:>100", type: REPOSITORY, first: 100) {
      nodes {
        ... on Repository {
          name
          stargazerCount
          createdAt
        }
      }
    }
  }
"""

result = run(rq01_query)

repositories = result["data"]["search"]["nodes"]

print(format(repositories))