from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list_or_create),
    path('<int:reviewPk>/', views.review_detail_like_or_update_delete),
    path('comment/', views.create_comment),
    path('comment/<int:commentPk>/', views.comment_delete),
]
