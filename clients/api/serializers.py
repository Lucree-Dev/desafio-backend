from rest_framework.serializers import Serializer, ModelSerializer
from clients.models import Client
from rest_framework import serializers

class ClientSerializer(Serializer):
    first_name = serializers.CharField(max_length=30, source="name")
    last_name = serializers.CharField(max_length=70, source="lastname")
    birthday = serializers.DateField()
    password = serializers.CharField(max_length=30, allow_blank=False)
    username = serializers.CharField(source="user.username")

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'birthday', 'username', 'user_id')
