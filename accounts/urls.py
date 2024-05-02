from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
from . import views

urlpatterns = [
    path('', views.UserManagement.as_view()),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('<str:username>/', views.UserDetail.as_view()),
    path("", views.AccountAPIView.as_view(), name="register"),
    path("<str:username>/", views.AccountDetailAPIView.as_view(), name="profile"),
    path("<str:username>/password/", views.AccountDetailPasswordAPIView.as_view(), name="password"),
    path("follow/<str:username>/", views.FollowAPIView.as_view())
]