from django.urls import path

from payment.apps import PaymentConfig
from payment.views import PaymentListView, PaymentCreateView

app_name = PaymentConfig.name

urlpatterns = [
    path('', PaymentListView.as_view(), name='payment_list'),
    path('create/<int:pk>/', PaymentCreateView.as_view(), name='payment_create'),
]
