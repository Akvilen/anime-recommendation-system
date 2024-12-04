import requests

ANILIST_API_URL = "https://graphql.anilist.co/"

def fetch_anime_by_name(name):
    query = """
    query ($name: String) {
      Media(search: $name, type: ANIME) {
        id
        title {
          english
          native
        }
        genres
        averageScore
        coverImage {
          extraLarge
        }
      }
    }
    """
    response = requests.post(ANILIST_API_URL, json={"query": query, "variables": {"name": name}})
    return response.json()
