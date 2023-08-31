from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from course.models import Course, Subscription
from course.paginators import CoursePaginator
from course.serializers import CourseSerializer, SubscriptionSerializer
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet to display the list of all courses.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    pagination_class = CoursePaginator

    def perform_create(self, serializer):
        """
        Save the owner during the creation.
        """
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwner]

        return [permission() for permission in permission_classes]


class SubscriptionCreateAPIView(CreateAPIView):
    """
    API View to create a subscription.
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the owner during the creation.
        """
        new_sub = serializer.save()
        new_sub.user = self.request.user
        new_sub.save()


class SubscriptionDeleteAPIView(DestroyAPIView):
    """
    API View to delete a subscription.
    """
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]
