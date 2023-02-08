from django.db import models
from clients.models import Client
from src.shared.models import BaseModel

class Card(BaseModel):
    title = models.CharField(max_length=50, default="")
    pan = models.CharField(max_length=19, blank=False, null=False, default="", unique=True)
    expiry_mm = models.CharField(max_length=2, blank=False, null=False, default="")
    expiry_yyyy = models.CharField(max_length=4, blank=False, null=False, default="")
    security_code = models.CharField(max_length=3, blank=False, null=False, default="")

    def __str__(self) -> str:
        return "{} - {}".format(self.title, self.pan)


class ClientCard(BaseModel):
    card = models.OneToOneField(Card, on_delete=models.CASCADE,  blank=False, null=False, default="")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False, default="")