from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.update),
    path('profile/<str:username>/', views.profile_or_delete_account),
    path('change_password/', views.ChangePasswordView.as_view()),
    path('userInfo/',views.user_detail),
]
