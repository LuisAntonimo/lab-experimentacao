from graphql import run_query


rq02_query = """
  {
    query SearchRepositories($queryString: String!, $first: Int!, $after: String){
      search(query: "stars:>100", type: REPOSITORY, first: 100) {
        nodes {
          ... on Repository {
            name
            stargazerCount
            pullRequests(states: MERGED) {
              totalCount
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

run_query(rq02_query)
