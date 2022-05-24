from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404


from .models import Movie, Genre
from .serializers import MovieSummarySerializer, MovieDetailSerializer
from django.db.models import Avg, Q

@api_view(['GET'])
def movie_list(request):
    # 랜덤 장르 3개, 장르별 영화 24개
    genre_id = request.GET.get('genre_id')

    # 중복 제거
    # user = request.user
    # reviews = user.reviews.all()
    # my_movies = user.my_movies.all()
    # .filter(~Q(pk__in=my_movies) & ~Q(reviews__in=reviews))
    movies = Movie.objects.filter(genre_ids=genre_id).order_by('?')[:24]

    serializer = MovieSummarySerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def mymovie_create_or_delete(request):
    movie_pk = request.data.get('moviePk')
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.user.filter(pk=user.pk).exists():
        movie.user.remove(user)
    else:
        movie.user.add(user)
    my_movies = user.my_movies.all()
    serializer = MovieSummarySerializer(my_movies, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_recommends(request):
    user = request.user
    # 자신이 평점을 3점 이상으로 부여한 리뷰 리스트를 불러온다.
    reviews = user.reviews.filter(rate__gte=3)
    if user.reviews.filter(rate__gte=3).exists:
        movie_list = []
        genre_list = []
        for review in reviews:
            # 해당 리뷰가 어떤 영화의 리뷰인지 저장한다.
            if review.movie not in movie_list:
                movie_list.append(review.movie)
            # 해당 리뷰의 영화가 어떤 장르인지 저장한다.
            now_genres = review.movie.genre_ids.all()
            for now_genre in now_genres:
                if now_genre not in genre_list:
                    genre_list.append(now_genre)

    user_list = []
    # 해당 영화들을 
    for movie in movie_list:
        # 3점 이상으로 평가한 리뷰를 뽑고
        reviews = movie.reviews.filter(rate__gte=3)
        for review in reviews:
            # 해당 리뷰를 작성한 유저를 뽑는다.
            if review.user not in user_list:
                user_list.append(review.user)

    # 그 유저들이 3점 이상으로 평가한 영화들의 전체 목록을 뽑고
    recommended_movies = []
    for user in user_list:
        reviews = user.reviews.filter(rate__gte=3)
        for review in reviews:
            movie = review.movie
            if movie not in recommended_movies:
                recommended_movies.append(movie)


    # list 를 queryset으로 변경
    def list_to_queryset(model, data):
        from django.db.models.base import ModelBase
        if not isinstance(model, ModelBase):
            raise ValueError(
                "%s must be Model" % model
            )
        if not isinstance(data, list):
            raise ValueError(
                "%s must be List Object" % data
            )
        pk_list = [obj.pk for obj in data]
        return model.objects.filter(pk__in=pk_list)

    recommended_movies = list_to_queryset(Movie, recommended_movies)


    # 해당 유저가 리뷰를 단 영화 & 내 영화 리스트에 추가한 영화 제거 & 24개로 제한 
    user = request.user
    reviews = user.reviews.all()
    my_movies = user.my_movies.all()

    recommended_movies = recommended_movies.filter(~Q(pk__in=my_movies) & ~Q(reviews__in=reviews))[:24]

    # 영화 목록
    # Field Lookup Django
    # Movie.objects.filter('어떤 조건').annotate(rate_average=Avg('reviews__rank'))
    recommended_movies = list(recommended_movies.annotate(rate_average=Avg('reviews__rate')))

    # # 0.3*vote_average/2 + 0.7*rate 로 별도의 점수를 만들어서 높은 순으로 출력한다. 
    recommended_movies.sort(key=lambda x : -(0.3*x.vote_average/2 + 0.7*x.rate_average))

    # order check
    # for recommended_movie in recommended_movies:
    #     print(0.3*recommended_movie.vote_average/2 + 0.7*recommended_movie.rate_average)

    # 만약 이런 방식의 추천 영화의 개수가 24 미만이라면 
    # (3점 이상으로 평가한 영화들의 장르)에서의 추천 영화로 추가해준다.
    need_number = 24 - len(recommended_movies)
    if need_number:
        import random 
        if genre_list:
            now_genre = random.sample(genre_list, 1)[0]
        else:
            genre_list = Genre.objects.all()
            now_genre = random.sample(genre_list, 1)[0]

        user = request.user
        reviews = user.reviews.all()
        my_movies = user.my_movies.all()
        # 중복 제거 & 투표순 정렬 
        genre_recommended_movies = now_genre.genres.filter(~Q(pk__in=my_movies) & ~Q(reviews__in=reviews)).order_by('-vote_average')[:need_number]
        recommended_movies.extend(list(genre_recommended_movies))


    serializer = MovieSummarySerializer(recommended_movies, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def movie_search(request):
    search_input = request.GET.get('userInput')
    search_output = Movie.objects.filter(title__contains=search_input)
    if search_output:
        serializer = MovieSummarySerializer(search_output, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def movie_detail(request, moviePk):
    movie = get_object_or_404(Movie, pk=moviePk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)