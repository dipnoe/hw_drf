from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Lesson(models.Model):
    """
    Model representing a lesson.

    Fields:
    - name (CharField): The name of the lesson.
    - description (TextField): Description of the lesson.
    - preview (ImageField): Preview image of the lesson.
    - video_link (URLField): Link to the lesson video.
    - course (ForeignKey): ForeignKey to model Course.
    - owner (ForeignKey): The owner of the lesson.
    """
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(verbose_name='первью', **NULLABLE)
    video_link = models.URLField(max_length=200, verbose_name='ссылка на видео', **NULLABLE)

    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, related_name='lessons',
                               verbose_name='курс', **NULLABLE)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
