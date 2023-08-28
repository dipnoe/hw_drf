from rest_framework import serializers

from course.models import Course
from lesson.serializers import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Course model.

    Fields:
    - name (CharField): The name of the course.
    - description (TextField): Description of the course.
    - preview (ImageField): Preview image of the course.
    - lesson_count (SerializerMethodField): The amount of lessons belongs to this course.
    """
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, required=False)

    class Meta:
        model = Course
        fields = ('name', 'description', 'preview', 'lesson_count', 'lessons')

    def get_lesson_count(self, instance):
        return instance.lessons.count()
