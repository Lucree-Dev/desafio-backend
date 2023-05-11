from django.db import models
from clients.models import Client
from cards.models import BillingCard


class Transfer(models.Model):
    friend = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False, default='')
    total_to_pay = models.IntegerField(blank=False, null=False, default=0)
    billing_card = models.ForeignKey(BillingCard, on_delete=models.CASCADE, blank=False, null=False, default='')
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.date} {self.total_to_pay}: {self.friend.first_name} to {self.billing_card.client.first_name}"
