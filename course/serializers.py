from rest_framework import serializers

from course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Course model.

    Fields:
    - name (CharField): The name of the course.
    - description (TextField): Description of the course.
    - preview (ImageField): Preview image of the course.
    """
    class Meta:
        model = Course
        fields = '__all__'
