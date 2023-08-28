from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import *

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user_list'),
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),

    # paths to get a token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]
