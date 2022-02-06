import requests

MOVIES_BASE_URL = 'https://www.omdbapi.com/'
API_KEY = '7cbb4cea'

def get_movie(title: str, year: int, _format: str='json') -> dict:
    params = {
        'apikey': API_KEY,
        't': title,
        'y': year,
        'r': _format
    }

    movie = requests.get(MOVIES_BASE_URL, params=params)
    return movie.json()
