from graphql import run_query

rq04_query = """
  {
    search(query: "stars:>100", type: REPOSITORY, first: 100) {
      nodes {
        ... on Repository {
          name
          stargazerCount
          createdAt
          updatedAt
        }
      }
    }
  }
"""

run_query(rq04_query)