from graphql import run_query

rq05_query = """
  {
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
    }
  }
"""

run_query(rq05_query)