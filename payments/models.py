from django.db import models
from src.shared.models import BaseModel
from clients.models import Client
from cards.models import ClientCard


class Transfers(BaseModel):
    friend = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False, default="")
    total_to_transfer = models.IntegerField(blank=False, null=False, default=0)
    client_card = models.ForeignKey(ClientCard, on_delete=models.CASCADE, blank=False, null=False, default="")

    def __str__(self) -> str:
        return "{}: {} to {}".format(self.friend.name, self.client_card.client.name)