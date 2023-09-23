import datetime

from celery import shared_task
from django.core.mail import send_mail

from config import settings


@shared_task
def send_sub_mail(course, email):
    send_mail(
        "Подписка на рассылку оформлена",
        f"Вы успешно подписались на обновления курса {course}",
        settings.EMAIL_HOST_USER,
        [email]
    )
    return "Отправлено"
