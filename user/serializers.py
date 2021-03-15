from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
        }
