from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Payment(models.Model):
    """
    Model representing a payment.

    Fields:
    - user (ForeignKey): The user who made the payment.
    - payment_date (DateField): The date of payment.
    - payment_amount (PositiveIntegerField): The amount.
    - payment_method (CharField): Cash or transfer to account.
    - paid_course (ForeignKey): Paid course.
    - paid_lesson (ForeignKey): Paid lesson.
    """

    PAYMENT_METHOD = [
        ('CASH', 'CASH'),
        ('TRANSFER', 'TRANSFER')
    ]

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='пользователь', related_name='users')

    payment_date = models.DateField(verbose_name='дата оплаты')
    payment_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=15, verbose_name='способ оплаты', choices=PAYMENT_METHOD)

    paid_course = models.ForeignKey('course.Course', on_delete=models.SET_NULL,
                                    verbose_name='оплаченный курс', related_name='courses', **NULLABLE)
    paid_lesson = models.ForeignKey('lesson.Lesson', on_delete=models.SET_NULL,
                                    verbose_name='оплаченный урок', related_name='lessons', **NULLABLE)

    def __str__(self):
        return f'{self.user} ({self.payment_amount} | {self.payment_date}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
