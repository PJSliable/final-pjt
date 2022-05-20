from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list),
    path('<int:moviePk>/', views.review_create),
    path('<int:moviePk>/<int:reviewPk>/', views.review_detail_like_or_update_delete),
    path('review/<int:reviewPk>/', views.create_comment),
    path('review/<int:reviewPk>/<int:commentPk>/', views.comment_delete),
]
