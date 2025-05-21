import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

if not API_KEY:
    raise ValueError("TMDB_API_KEY is not set in .env file")

BASE_URL = "https://api.themoviedb.org/3"

def fetch_movies(category: str = "popular", page: int = 1):
    url = f"{BASE_URL}/movie/{category}"
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "page": page
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()