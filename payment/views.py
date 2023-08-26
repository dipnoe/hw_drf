from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from payment.models import Payment
from payment.serializers import PaymentSerializer


class PaymentListView(ListAPIView):
    """
    API View for display the list of all payments.
    It's available for ordering by payment date and filtering by payment method, paid courses and paid lessons.
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['payment_method', 'paid_course', 'paid_lesson']
    ordering_fields = ['payment_date']
