from graphql import run_query


rq02_query = """
  {
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
    }
  }
"""

run_query(rq02_query)
