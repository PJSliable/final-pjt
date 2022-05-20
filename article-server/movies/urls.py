from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('recommends/', views.movie_recommends),
    path('mymovie/', views.mymovie_create_or_delete),
    path('search/',views.movie_search),
    path('<int:moviePk>/', views.movie_detail),

]
