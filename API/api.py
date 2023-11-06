import requests
from django.conf import settings

# Replace 'YOUR_API_KEY' with your TMDb API key
API_KEY = settings.TMDB_API_KEY

# Base URL for TMDb API
BASE_URL = 'https://api.themoviedb.org/3'

def discover_movies():
    endpoint = f'{BASE_URL}/discover/movie'
    params = {
        'api_key': API_KEY,
        'sort_by': 'popularity.desc',  # You can change the sorting criteria
        # 'with_genres': '28',  # Change this to the desired genre ID (e.g., 28 for Action)
        'release_date.gte': '2022-01-01',  # Change the release date range as needed
    }

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
        # if data['results']:
        #     for movie in data['results']:
        #         print(f"Title: {movie['title']}")
        #         print(f"Release Date: {movie['release_date']}")
        #         print(f"Overview: {movie['overview']}")
        #         print("--------------")
        # else:
        #     print("No movies found.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# if __name__ == '__main__':
#     discover_movies()

def search(name):
    base_url = 'https://api.themoviedb.org/3'

    search_endpoint = '/search/movie'

    # Construct the URL for the search request
    url = f'{base_url}{search_endpoint}?api_key={API_KEY}&query={name}'


    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    return data


def findMovie(id):
    url = f'https://api.themoviedb.org/3/movie/{id}?&append_to_response=videos,credits&api_key={API_KEY}'
    
    response = requests.get(url)
    movie_data = response.json()
    
    return movie_data