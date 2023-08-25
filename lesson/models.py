from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(verbose_name='первью', **NULLABLE)
    video_link = models.URLField(max_length=200, verbose_name='ссылка на видео', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
