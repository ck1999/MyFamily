from rest_framework import serializers

from .models import custom_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = custom_user_model
        fields = [
            "id",
            "full_name",
            "get_image",
        ]