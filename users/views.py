from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView

from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
