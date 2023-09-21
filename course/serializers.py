from rest_framework import serializers

from course.models import Course, Subscription
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
    is_subscribe = serializers.SerializerMethodField()

    class Meta:
        model = Course
        # fields = ('name', 'description', 'preview', 'is_subscribe', 'lesson_count', 'lessons')
        fields = '__all__'

    def get_lesson_count(self, instance):
        return instance.lessons.count()

    def get_is_subscribe(self, instance):
        request = self.context['request']
        subscription = Subscription.objects.filter(course=instance, user=request.user)
        return True if subscription else False


class SubscriptionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Subscription model.

    Fields:
    - course (ForeignKey): The course associated with the subscription.
    - user (ForeignKey): The user who subscribed to the course.
    """
    class Meta:
        model = Subscription
        fields = '__all__'
