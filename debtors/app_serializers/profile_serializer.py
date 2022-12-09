from rest_framework import serializers
from ..app_models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'department', 'position', 'birthday', 'is_deleted']