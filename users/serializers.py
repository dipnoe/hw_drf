from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.

    Fields:
    - email (EmailField): Email address of the user. Used for authentication.
    - phone (PositiveIntegerField): Phone number of the user.
    - city (CharField): City where the user is located.
    - avatar (ImageField): Avatar image of the user.
    """
    class Meta:
        model = User
        fields = '__all__'
