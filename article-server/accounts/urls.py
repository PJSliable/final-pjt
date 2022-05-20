from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.update),
    path('change_password/', views.ChangePasswordView.as_view()),
    path('profile/<str:username>/', views.profile_or_delete_account),
]
