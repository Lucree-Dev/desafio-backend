from rest_framework import serializers
from .models import card

class CardSerializer(serializers.ModelSerializer):

    class Meta:

        model = card
        fields = '__all__'