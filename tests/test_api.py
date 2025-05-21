from tmdb_cli import api

def test_search_movies_returns_results():
    result = api.search_movies("Inception")
    assert "results" in result
    assert len(result["results"]) > 0