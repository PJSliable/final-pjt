from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('mymovie/', views.mymovie_create_or_delete),
    path('recommends/', views.movie_recommends),
    path('search/',views.movie_search),
    path('<int:moviePk>/', views.movie_detail),
    path('<int:moviePk>/community/', views.review_create),
    path('<int:moviePk>/community/<int:reviewPk>/', views.review_management)

]
