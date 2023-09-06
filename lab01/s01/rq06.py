from graphql import run_query

rq06_query = """
  query ($after: String){
    search(query: "stars:>100", type: REPOSITORY, first: 100, after: $after) {
        edges {
          node {
            ... on Repository {
              name
              stargazerCount
              total_issues: issues {
                totalCount
              }
              closed_issues: issues(states: CLOSED) {
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

run_query(rq06_query, 'rq06', ["Repository", "Stars", "% of Closed Issues"])
