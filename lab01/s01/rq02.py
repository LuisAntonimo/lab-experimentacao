from graphql import run_query

rq02_query = """
    query ($after: String){
      search(query: "stars:>100", type: REPOSITORY, first: 100, after: $after) {
        edges {
         node {
          ... on Repository {
            name
            stargazerCount
            pullRequests(states: MERGED) {
              totalCount
            }
          }
         }
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
"""

run_query(rq02_query, 'rq02', ["Repository", "Stars", "Merged PR's"])