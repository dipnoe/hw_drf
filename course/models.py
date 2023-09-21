from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """
    Model representing a course.

    Fields:
    - name (CharField): The name of the course.
    - description (TextField): Description of the course.
    - preview (ImageField): Preview image of the course.
    - owner (ForeignKey): The owner of the course.
    """
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(verbose_name='первью', **NULLABLE)
    price = models.PositiveIntegerField(verbose_name='цена', default=2000)

    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Subscription(models.Model):
    """
    Model representing a subscription.

    Fields:
    - course (ForeignKey): The course associated with the subscription.
    - user (ForeignKey): The user who subscribed to the course.
    """
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, verbose_name='курс')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.user} подписался на обновления курса {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
