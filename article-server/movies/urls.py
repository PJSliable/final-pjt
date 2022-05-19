from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/mymovie/', views.mymovie_list),
    path('movies/recommends/', views.movie_recommends),
    path('movies/search/',views.movie_search),
    path('movies/<int:moviePk>/', views.movie_detail),
    path('/<int:moviePk>/community/', views.review_create),
    path('/:moviePk/community/<int:reviewPk>/', views.review_management)

]
