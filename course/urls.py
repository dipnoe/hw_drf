from django.urls import path
from rest_framework.routers import DefaultRouter

from course.apps import CourseConfig
from course.views import *

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
      path('course/subscription/create/', SubscriptionCreateAPIView.as_view(), name='create_subscription'),
      path('course/subscription/delete/<int:pk>/', SubscriptionDeleteAPIView.as_view(), name='delete_subscription'),
] + router.urls
