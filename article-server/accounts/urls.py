from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.update),
    path('change_password/', views.change_password),
    path('profile/<str:username>/', views.profile),
]
