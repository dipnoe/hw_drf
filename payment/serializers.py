from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Lesson model.

    Fields:
    - user (ForeignKey): The user who made the payment.
    - payment_date (DateField): The date of payment.
    - payment_amount (PositiveIntegerField): The amount.
    - payment_method (CharField): Cash or transfer to account.
    - paid_course (ForeignKey): Paid course.
    - paid_lesson (ForeignKey): Paid lesson.
    """

    class Meta:
        model = Payment
        fields = '__all__'
