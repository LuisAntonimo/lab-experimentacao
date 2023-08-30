from graphql import run_query

rq04_query = """
  {
    query SearchRepositories($queryString: String!, $first: Int!, $after: String){
      search(query: "stars:>100", type: REPOSITORY, first: 100) {
        nodes {
          ... on Repository {
            name
            stargazerCount
            createdAt
            updatedAt
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

run_query(rq04_query)