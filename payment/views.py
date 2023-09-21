import datetime
from os import getenv
from dotenv import load_dotenv

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
import stripe

from course.models import Course
from payment.models import Payment
from payment.serializers import PaymentSerializer

load_dotenv()


class PaymentListView(ListAPIView):
    """
    API View for display the list of all payments.
    It's available for ordering by payment date and filtering by payment method, paid courses and paid lessons.
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['payment_method', 'paid_course', 'paid_lesson']
    ordering_fields = ['payment_date']


class PaymentCreateView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        course = Course.objects.get(id=kwargs.get('pk'))
        stripe.api_key = getenv('STRIPE_API')

        response = stripe.PaymentIntent.create(
            amount=course.price,
            currency="usd",
            automatic_payment_methods={
                "enabled": True,
                "allow_redirects": "never"
            },
        )

        stripe.PaymentIntent.confirm(
            response.id,
            payment_method="pm_card_visa"
        )

        data = stripe.PaymentIntent.retrieve(
            response.id
        )

        user = self.request.user
        payment = Payment.objects.create(
            user=user,
            payment_date=datetime.date.today(),
            payment_amount=course.price,
            payment_method='TRANSFER',
            paid_course=course
        )
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
