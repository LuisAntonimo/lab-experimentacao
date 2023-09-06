from graphql import run_query

rq04_query = """
  query ($after: String){
    search(query: "stars:>100", type: REPOSITORY, first: 100, after: $after) {
        edges {
          node {
            ... on Repository {
              name
              stargazerCount
              updatedAt
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

run_query(rq04_query,'rq04', ["Repository", "Stars", "Last Update (seconds)"])