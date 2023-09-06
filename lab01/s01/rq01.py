from graphql import run_query

rq01_query = """
  query ($after: String){
    search(query: "stars:>100", type: REPOSITORY, first: 100, after: $after) {
      edges {
        node {
          ... on Repository {
            name
            stargazerCount
          createdAt
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

run_query(rq01_query, 'rq01', ["Repository", "Stars", "Creation Date"])