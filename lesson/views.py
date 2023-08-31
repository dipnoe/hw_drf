from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from lesson.models import Lesson
from lesson.paginators import LessonPaginator
from lesson.serializers import LessonSerializer
from users.models import UserRole
from users.permissions import IsModerator, IsOwner


class LessonListAPIView(ListAPIView):
    """
    API View for display the list of all lessons.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LessonPaginator

    def get_queryset(self):
        """ Returns queryset depending on the user's role."""
        if self.request.user.role == UserRole.MODERATOR:
            queryset = Lesson.objects.all()
        else:
            queryset = Lesson.objects.filter(owner=self.request.user)
        return queryset


class LessonRetrieveAPIView(RetrieveAPIView):
    """
    API View to retrieve a single lesson.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonCreateAPIView(CreateAPIView):
    """
    API View to create a new lesson.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonUpdateAPIView(UpdateAPIView):
    """
    API View to update a lesson.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDeleteAPIView(DestroyAPIView):
    """
    API View to delete a lesson.
    """
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
