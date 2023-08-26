from django.shortcuts import render
from rest_framework import viewsets

from course.models import Course
from course.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet to display the list of all courses.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
