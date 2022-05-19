from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404


from .models import Genre, Movie, Review
from .serializers import MovieSummarySerializer, MovieDetailSerializer

import random

@api_view(['GET'])
def movie_list(request):
    # 랜덤 장르 3개, 장르별 영화 10개
    genre_id = request.GET.get('genre_id')
    movies = random.sample(Movie.objects.filter(genre_ids=genre_id), 10)
    serializer = MovieSummarySerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['POST','DELETE'])
def mymovie_create_or_delete(request):
    moviePk = request.GET.get('moviePk')
    movie = get_object_or_404(Movie, pk=moviePk)
    user = request.user

    def create_mymovie():
        movie.user.add(user)
        mymovies = Movie.objects.filter(user=user)
        serializer = MovieSummarySerializer(mymovies)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete_mymovie():
        movie.user.remove(user)
        mymovies = Movie.objects.filter(user=user)
        serializer = MovieSummarySerializer(mymovies)
        return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)

    if request.method == 'POST':
        return create_mymovie()
    elif request.method == 'DELETE':
        return delete_mymovie()

def movie_recommends(request):
    pass

def movie_search(request):
    pass

@api_view(['GET'])
def movie_detail(request,moviePk):
    movie = get_object_or_404(Movie, pk=moviePk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

def review_create(request):
    pass

def review_management(request):
    pass



# 참고 사항 json 보내는 2가지 방법
# 1
# @api_view(['POST'])
# def likes(request, pk):
#     article = get_object_or_404(Article,pk=pk)
#     user = request.user
#     response = {
#         'liked':False,
#         'count':0,
#     }
#     if article.like_users.filter(pk=user.pk).exists():
#         article.like_users.remove(user)
#     else:
#         article.like_users.add(user)
#         response['liked'] = True
#     response['count'] = article.like_users.count()
#     return JsonResponse(response)

# 2
# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == 'GET':
#         # articles = Article.objects.all()
#         articles = get_list_or_404(Article)
#         serializer = ArticleListSerializer(articles, many=True)
#         return Response(serializer.data)