from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsModerator
from users.serializers import UserSerializer


# Create your views here.
class UserListAPIView(ListAPIView):
    """
    API view for display the list of all users.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]


class UserCreateAPIView(CreateAPIView):
    """
    API view for update a user.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateAPIView(UpdateAPIView):
    """
    API view for update a user.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
