from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class CreateClientSerializer(serializers.Serializer):

    class Meta:
        model = Client
        fields = '__all__'


class AddFriendSerializer(serializers.Serializer):
    friend_name = serializers.CharField(source='user.username')