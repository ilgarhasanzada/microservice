from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from . import views

urlpatterns = [
    path('token/', views.DecoratedTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.DecoratedTokenRefreshView.as_view(), name='token_refresh'),
    path('token/decode/', views.TokenDecode.as_view(), name='token_decode'),
]