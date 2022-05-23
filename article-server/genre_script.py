import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")

import django
django.setup()

import requests
from movies.models import Genre

def save_genre_data():
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = '/genre/movie/list'
    params = {
        'api_key':'f6a4dc74497f9fa968f0457d06d75600',
        'language':'ko'
    }
    try:
        response = requests.get(BASE_URL+PATH, params = params)
        print(response)
        data = response.json()
        genres = data.get("genres")
        for genre in genres:
            print(genre)
            Genre.objects.create(
                id = genre['id'],
                name = genre['name']
            )
    except:
        return

if __name__ == '__main__':
    save_genre_data()