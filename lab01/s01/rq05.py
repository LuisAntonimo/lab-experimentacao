from graphql import run_query

rq05_query = """
  {
    query SearchRepositories($queryString: String!, $first: Int!, $after: String){
      search(query: "stars:>100", type: REPOSITORY, first: 100) {
        nodes {
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
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
  }
"""

run_query(rq05_query)