import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")

import django
django.setup()

import requests
# from django.conf import settings

from movies.models import Movie,Genre

# settings.configure(DEBUG=True)
"""
django 환경설정 필수 Using settings without setting DJANGO_SETTINGS_MODULE
https://docs.djangoproject.com/en/4.0/topics/settings/#using-settings-without-setting-django-settings-module

실행방법)
python script.py

manage.py => 장고 환경 관련 기능을 실행하게 해줌
"""

# 1. 수집한 데이터 불러오기
# API, CSV 파일..

def save_movie_data():
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = '/movie/popular'
    for page_number in range(1,1001):
        params = {
            'api_key':'f6a4dc74497f9fa968f0457d06d75600',
            'page' : page_number,
            'language':'ko',
        }
        print('page is', page_number)
        try:
            response = requests.get(BASE_URL+PATH, params = params)
            print(response)
            data = response.json()
            movies = data.get("results")

# 2. Article 테이블에 넣기
# Tip. 한 번에 여러 개 넣을 때는 bulk_create 사용
# for article in articles:
#     Article.objects.create(
#         title=article.title,
#         ...
#     )
            for movie in movies:
                print('movie is', movie)
            # 수정 필요함. 미완성
                if not movie.get('title', 0) or not movie.get('release_date', 0) or not movie.get('vote_average', 0) or not movie.get('overview', 0) or not movie.get('poster_path', 0) or not movie.get('backdrop_path', 0):
                    continue
                now_movie = Movie.objects.create(
                    title = movie['title'],
                    release_date = movie['release_date'],
                    vote_average = movie['vote_average'],
                    overview = movie['overview'],
                    poster_path = movie['poster_path'],
                    backdrop_path = movie['backdrop_path'],
                )
                for now in movie['genre_ids']:
                    genre = Genre.objects.get(pk=now)
                    now_movie.genre_ids.add(genre)
                now_movie.save()
        except:
            break

if __name__ == '__main__':
    save_movie_data()