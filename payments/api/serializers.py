from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from payments.models import Transfers


class CreateTransferSerializer(ModelSerializer):
    billing_card = serializers.DictField(child=serializers.CharField())

    class Meta:
        model = Transfers
        fields = ("friend_id", "total_to_transfer", "billing_card")


class ListTransfersSerializer(ModelSerializer):
    user_id = serializers.CharField(source="client_card.client_id")
    value = serializers.CharField(source="total_to_transfer")
    from_card = serializers.CharField(source="client_card.card_id")
    date = serializers.ReadOnlyField()

    class Meta:
        model = Transfers
        fields = ("user_id", "friend_id", "value", "from_card", "date")