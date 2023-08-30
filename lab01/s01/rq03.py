from graphql import run_query

rq03_query = """
  {
    query SearchRepositories($queryString: String!, $first: Int!, $after: String){
      search(query: "stars:>100", type: REPOSITORY, first: 100) {
        nodes {
          ... on Repository {
            name
            stargazerCount
            releases (orderBy: {field: CREATED_AT, direction: DESC}){
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

run_query(rq03_query)