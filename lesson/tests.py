from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course
from lesson.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def create_moderator(self):
        self.moderator = User.objects.create(
            email='moderator@test.test',
            role='moderator'
        )
        self.moderator.set_password('12345')
        self.moderator.save()

    def create_member(self):
        self.member = User.objects.create(
            email='member@test.test',
        )
        self.member.set_password('12345')
        self.member.save()

    def setUp(self):

        self.create_moderator()
        self.create_member()

        self.course = Course.objects.create(
            name='тестовый курс'
        )

        self.lesson = Lesson.objects.create(
            name='тестовый урок',
            course=self.course,
            owner=self.member
        )

    def test_get_list(self):
        """ Test for getting list of lessons. """
        self.client.force_authenticate(self.moderator)
        response = self.client.get(
            reverse('lesson:lesson_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 4,
                        "name": self.lesson.name,
                        "description": None,
                        "preview": None,
                        "video_link": None,
                        "course": self.course.pk,
                        "owner": self.member.pk
                    }
                ]
            }
        )

    def test_create_lesson(self):
        """ Test for creating the lesson. """
        data = {
            'name': 'test_create',
            'description': 'test description',
            'video_link': 'https://www.youtube.com/watch?v=ygwW-VnWeMI&ab_channel=Seether',
            'course': self.course.pk,
            'owner': self.member.pk
        }

        self.client.force_authenticate(self.member)

        response = self.client.post(
            reverse('lesson:lesson_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )

    def test_update_lesson(self):
        """ Test for updating the lesson. """
        data = {
            'name': 'test_upgrade',
            'description': 'test description',
            'video_link': 'https://www.youtube.com/watch?v=ygwW-VnWeMI&ab_channel=Seether',
            'course': self.course.pk,
            'owner': self.member.pk
        }

        self.client.force_authenticate(self.member)

        response = self.client.patch(
            reverse('lesson:lesson_update', kwargs={'pk': self.lesson.pk}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Lesson.objects.get(pk=self.lesson.pk).name,
            'test_upgrade'
        )

    def test_delete_lesson(self):
        """ Test for deleting the lesson. """
        self.client.force_authenticate(self.member)

        response = self.client.delete(
            reverse('lesson:lesson_delete', kwargs={'pk': self.lesson.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
