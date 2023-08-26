from django.core.management import BaseCommand
from random import randrange, choice

from course.models import Course
from lesson.models import Lesson
from payment.models import Payment
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        payment_list = [

            {"user": User.objects.get(id=2),
             "payment_date": choice(["2023-08-27", "2023-08-26", "2023-08-25", "2023-08-24"]),
             "payment_amount": randrange(1500, 5000, 500),
             "payment_method": choice(["CASH", "TRANSFER"]),
             "paid_course": Course.objects.get(id=5),
             "paid_lesson": Lesson.objects.get(id=3)},

            {"user": User.objects.get(id=2),
             "payment_date": choice(["2023-08-27", "2023-08-26", "2023-08-25", "2023-08-24"]),
             "payment_amount": randrange(1500, 5000, 500),
             "payment_method": choice(["CASH", "TRANSFER"]),
             "paid_course": Course.objects.get(id=5),
             "paid_lesson": None},

            {"user": User.objects.get(id=2),
             "payment_date": choice(["2023-08-27", "2023-08-26", "2023-08-25", "2023-08-24"]),
             "payment_amount": randrange(1500, 5000, 500),
             "payment_method": choice(["CASH", "TRANSFER"]),
             "paid_course": None,
             "paid_lesson": Lesson.objects.get(id=3)}

        ]

        for_create = []
        for payment in payment_list:
            for_create.append(
                Payment(**payment)
            )
        Payment.objects.bulk_create(for_create)
