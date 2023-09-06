from graphql import run_query

rq05_query = """
  query ($after: String){
    search(query: "stars:>100", type: REPOSITORY, first: 100, after: $after) {
        edges {
          node {
            ... on Repository {
              name
              stargazerCount
              languages(first: 2, orderBy: {field: SIZE, direction: DESC}) {
                edges {
                  node {
                    id
                    name
                  }
                }
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

run_query(rq05_query,'rq05', ["Repository", "Stars", "Language"])