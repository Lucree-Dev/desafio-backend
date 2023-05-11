from rest_framework.serializers import ModelSerializer
from .models import Card

class CardSerializer(ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'
