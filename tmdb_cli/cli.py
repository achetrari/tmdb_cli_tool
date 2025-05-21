import argparse 
from tabulate import tabulate
from tmdb_cli.api import fetch_movies

def main():
    parser = argparse.ArgumentParser(description="TMDB CLI Tool")
    parser.add_argument(
        "--type",
        choices=["playing", "popular", "top", "upcoming"],
        help="Category of movies to fetch"
    )
    args = parser.parse_args()
    print(f"\n🎬 Fetching movies for type: {args.type}\n")

    # Map CLI --type values to TMDB API endpoints
    type_to_endpoint = {
        "playing": "now_playing",
        "popular": "popular",
        "top": "top_rated",
        "upcoming": "upcoming"
    }

    category = type_to_endpoint[args.type]
    data = fetch_movies(category=category)
    results = data.get("results", [])

    if not results:
        print("⚠️ No results found.")
        return
    
    # Extract relevant fields and create table
    table = []
    for movie in results:
        title = movie.get("title", "N/A")
        release = movie.get("release_date", "N/A")
        rating = movie.get("vote_average", "N/A")
        table.append([title, release, rating])

    headers = ["Title", "Release Date", "Rating"]
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))