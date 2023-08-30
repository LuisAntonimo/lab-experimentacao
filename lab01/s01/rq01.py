from graphql import run_query

rq01_query = """
  {
    query SearchRepositories($queryString: String!, $first: Int!, $after: String){
      search(query: "stars:>100", type: REPOSITORY, first: 100) {
        nodes {
          ... on Repository {
            name
            stargazerCount
           createdAt
          }
        }
        pageInfo {
          endCursor
          hasNextPage
      }
    }
  }
"""

run_query(rq01_query)