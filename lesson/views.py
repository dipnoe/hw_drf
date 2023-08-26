from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from lesson.models import Lesson
from lesson.serializers import LessonSerializer


class LessonListAPIView(ListAPIView):
    """
    API View for display the list of all lessons.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(RetrieveAPIView):
    """
    API View to retrieve a single lesson.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateAPIView(CreateAPIView):
    """
    API View to create a new lesson.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateAPIView(UpdateAPIView):
    """
    API View to update a lesson.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDeleteAPIView(DestroyAPIView):
    """
    API View to delete a lesson.
    """
    queryset = Lesson.objects.all()
