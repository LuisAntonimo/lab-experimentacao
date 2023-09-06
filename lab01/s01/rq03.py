from graphql import run_query

rq03_query = """
  query ($after: String){
    search(query: "stars:>100", type: REPOSITORY, first: 100, after: $after) {
        edges {
          node {
            ... on Repository {
              name
              stargazerCount
              releases (orderBy: {field: CREATED_AT, direction: DESC}){
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

run_query(rq03_query,'rq03', ["Repository", "Stars", "Total Releases"])