from graphql import run_query

rq06_query = """
  {
    query SearchRepositories($queryString: String!, $first: Int!, $after: String){
      search(query: "stars:>100", type: REPOSITORY, first: 100) {
        nodes {
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
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
  }
"""

run_query(rq06_query)
