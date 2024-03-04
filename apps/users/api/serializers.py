from rest_framework.serializers import ModelSerializer

from apps.users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "fullname",
            "age",
            "job",
            "gender",
            "phone_number",
            "instagram",
            "tiktok",
            "email",
            
        ]
        