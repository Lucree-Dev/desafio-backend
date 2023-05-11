from django.db import models
from clients.models import Client

class Card(models.Model):
    card_id = models.CharField(max_length=90, primary_key=True)
    title = models.CharField(max_length=60, default='')
    pan = models.CharField(max_length=16, blank=False, null=False, default='', unique=True)
    expiry_mm = models.CharField(max_length=2, blank=False, null=False, default='')
    expiry_yyyy = models.CharField(max_length=4, blank=False, null=False, default='')
    security_code = models.CharField(max_length=4, blank=False, null=False, default='')
    date = models.DateField(auto_now=True)

    def __repr__(self) -> str:
        return f"{self.title} - {self.pan}"

    def __str__(self) -> str:
        return f"{self.title} - {self.pan}"

class BillingCard(models.Model):
    card = models.OneToOneField(Card, on_delete=models.CASCADE,  blank=False, null=False, default='')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False, default='')
