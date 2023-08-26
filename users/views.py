from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView

from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class UserListAPIView(ListAPIView):
    """
    API view for display the list of all users.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    """
    API view for update a user.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
