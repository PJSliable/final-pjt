from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404


from .models import Movie
from .serializers import MovieSummarySerializer, MovieDetailSerializer


@api_view(['GET'])
def movie_list(request):
    # 랜덤 장르 3개, 장르별 영화 24개
    genre_id = request.GET.get('genre_id')
    movies = Movie.objects.filter(genre_ids=genre_id).order_by('?')[:24]
    # mymovie인 경우에 제외하기 
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





# 자신이 평점을 3점 이상으로 리뷰를 단 영화들의 목록과 장르를 받는다. 
# 해당 영화들을 마찬가지로 3점 이상으로 평가한 유저들의 목록을 뽑아 해당 유저들이 3점 이상으로 평가한 영화들을 파악하고
# 0.3*vote_average/2 + 0.7*rate 로 별도의 점수를 만들어서 높은 순으로 출력한다. 총점 3점 이상이여야 함.
# 만약 이런 방식의 추천 영화의 개수가 24 미만이라면 3점 이상으로 평가한 영화들의 장르를 파악하고 해당 장르에서의 추천 영화로 추가해준다.
# 만약 이런 방식으로도 24개를 못채운다면
@api_view(['GET'])
def movie_recommends(request):
    user = request.user
    reviews = user.reviews.filter(rate__gte=3)
    genre_list = []
    for review in reviews:
        now_genres = review.movie.genre_ids
        for now_genre in now_genres:
            if now_genre not in genre_list:
                genre_list.append(now_genre)
    ## 여기까지 완료함.
    
    user_list = []
    # 각 영화마다 해당 영화를 좋아하는 유저들의 목록을 받아와 저장한다.
    for my_movie in my_movies:
        now_users = my_movie.like_users.all()
        for now_user in now_users:
            # 유저 중복 제거
            if now_user not in user_list:
                user_list.append(now_user)
    # 본인 제거
    user_list.remove(user)
    
    # 해당 유저들이 좋아하는 영화들을 가져와 저장한다.
    recommended_movies = []
    for movie_like_user in user_list:
        now_movies = Movie.objects.filter(like_users=movie_like_user.pk)
        for now_movie in now_movies:
            # 영화 중복 제거
            if now_movie not in recommended_movies:
                recommended_movies.append(now_movie)
    # 자신이 본 영화 제거
    for my_movie in my_movies:
        if my_movie in recommended_movies:
            recommended_movies.remove(my_movie)
    # 영화를 평점을 기준으로 정렬 (상위 평점 순으로 정렬하여 추천)
    recommended_movies.sort(key=lambda x : -x.vote_average)
	# 영화 개수가 10개를 초과하지 않게 제한
    recommended_movies = recommended_movies[:10]
    # 만약에 영화의 개수가 10개보다 적다면 그냥 전체 영화에서 평점 상위 10개의 목록을 가져와 순서대로 빈 자리만큼 채워주기
    add_movies = Movie.objects.order_by('-vote_average')[:10]
    for add_movie in add_movies:
        # 개수가 10개가 될 때 break
        if len(recommended_movies) >= 10:
            break
        if add_movie not in recommended_movies:
            recommended_movies.append(add_movie)

    context = {
        'recommended_movies': recommended_movies,
    }
    return JsonResponse(request, 'movies/recommended.html', context)






@api_view(['GET'])
def movie_search(request):
    search_input = request.GET.get('userInput')
    search_output = Movie.objects.filter(title__contains=search_input)
    if search_output:
        serializer = MovieSummarySerializer(search_output, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail(request, moviePk):
    movie = get_object_or_404(Movie, pk=moviePk)
    serializer = MovieDetailSerializer(movie)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)


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