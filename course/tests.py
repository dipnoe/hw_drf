from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course, Subscription
from users.models import User


class SubscriptionTestCase(APITestCase):

    def setUp(self) -> None:
        self.course = Course.objects.create(
            name='тестовый курс'
        )

        self.user = User.objects.create(
            email='test@test.test'
        )
        self.user.set_password('12345')
        self.user.save()

        self.subscription = Subscription.objects.create(
            course=self.course,
            user=self.user
        )

    def test_create_subscription(self):
        """ Test for creating the subscription. """
        data = {
            'course': self.course.pk,
            'user': self.user.pk
        }

        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('course:create_subscription'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Subscription.objects.all().count(),
            2
        )

    def test_delete_subscription(self):
        """ Test for deleting the subscription. """
        self.client.force_authenticate(self.user)

        response = self.client.delete(
            reverse('course:delete_subscription', kwargs={'pk': self.subscription.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
