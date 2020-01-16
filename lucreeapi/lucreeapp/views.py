from django.shortcuts import render
from .models import person, card, cards, friends, bank_statement
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_condition import Or
from rest_framework.authentication import SessionAuthentication
from .serializers import CardSerializer

# Create your views here.

class CardList(generics.ListCreateAPIViews):

    queryset = card.objects.all()
    serializer_class = CardSerializer
    
