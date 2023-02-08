from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from cards.models import Card
from datetime import datetime

class CardSerializer(ModelSerializer):
    card_id = serializers.CharField(source="id", allow_null=True)
    date = serializers.SerializerMethodField(read_only=True)

    def get_date(self, obj): 
        if "created_at" in obj: 
            created_at = obj["created_at"]
            return datetime.strftime(created_at, "%d/%m/%Y")

        return None

    class Meta:
        model=Card
        fields=('card_id', 'title', 'pan', 'expiry_mm', 'expiry_yyyy', 'security_code', 'date')