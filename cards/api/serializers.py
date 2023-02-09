from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from cards.models import Card
from datetime import datetime

class CardSerializer(ModelSerializer):
    card_id = serializers.CharField(source="id", allow_null=True)
    date = serializers.SerializerMethodField(read_only=True)

    def get_date(self, obj): 
        created_at = None

        if isinstance(obj, object) and hasattr(obj, "created_at"):
            created_at = obj.created_at
        elif isinstance(obj, dict) and "created_at" in obj: 
            created_at = obj["created_at"]
      
        return created_at

    class Meta:
        model=Card
        fields=('card_id', 'title', 'pan', 'expiry_mm', 'expiry_yyyy', 'security_code', 'date')