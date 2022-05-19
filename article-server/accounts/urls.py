from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/',views.logout),
    path('update/', views.update),
    path('change_password/', views.change_password),
    path('profile/<str:username>/', views.profile),
]
