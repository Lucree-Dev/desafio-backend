from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Transfer


class CreateTransferSerializer(ModelSerializer):
    billing_card = serializers.DictField(child=serializers.CharField())

    class Meta:
        model = Transfer
        fields = ("date", "friend_id", "total_to_pay", "billing_card")


class ListTransfersSerializer(ModelSerializer):
    user_id = serializers.CharField(source='billing_card.client_id')
    value = serializers.CharField(source='total_to_pay')
    from_card = serializers.CharField(source='billing_card.card_id')
    date = serializers.ReadOnlyField()

    class Meta:
        model = Transfer
        fields = ('user_id', 'friend_id', 'value', 'from_card', 'date')
