from graphql import run_query

rq01_query = """
  {
    search(query: "stars:>100", type: REPOSITORY, first: 100) {
      nodes {
        ... on Repository {
          name
          stargazerCount
          createdAt
        }
      }
    }
  }
"""

run_query(rq01_query)