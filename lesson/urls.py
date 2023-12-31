from django.urls import path

from lesson.apps import LessonConfig
from lesson.views import *

app_name = LessonConfig.name

urlpatterns = [
    path('', LessonListAPIView.as_view(), name='lesson_list'),
    path('<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('<int:pk>/delete/', LessonDeleteAPIView.as_view(), name='lesson_delete'),
]
