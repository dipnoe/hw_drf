from rest_framework import serializers

from lesson.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """
    Serializer for the Lesson model.

    Fields:
    - name (CharField): The name of the lesson.
    - description (TextField): Description of the lesson.
    - preview (ImageField): Preview image of the lesson.
    - video_link (URLField): Link to the lesson video.
    """
    class Meta:
        model = Lesson
        fields = '__all__'
