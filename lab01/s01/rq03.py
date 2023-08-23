from graphql import run_query

rq03_query = """
  {
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
    }
  }
"""

run_query(rq03_query)