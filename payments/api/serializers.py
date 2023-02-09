from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from payments.models import Transfers


class CreateTransferSerializer(ModelSerializer):
    billing_card = serializers.DictField(child=serializers.CharField())

    class Meta:
        model = Transfers
        fields = ("friend_id", "total_to_transfer", "billing_card")