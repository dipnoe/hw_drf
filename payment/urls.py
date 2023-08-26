from django.urls import path

from payment.apps import PaymentConfig
from payment.views import PaymentListView

app_name = PaymentConfig.name

urlpatterns = [
    path('', PaymentListView.as_view(), name='payment_list'),
]
