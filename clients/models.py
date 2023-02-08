from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date
from src.shared.models import BaseModel

class Client(BaseModel):
    name = models.CharField(max_length=30, blank=False, null=False, default="")
    lastname = models.CharField(max_length=70, blank=False, null=False, default="")
    birthday = models.DateField(max_length=timezone.now(), default=timezone.now())
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False, default="")

    def __str__(self) -> str:
        return "{} {}".format(self.name, self.lastname)


class ClientFriends(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='%(class)s_client')
    friend = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='%(class)s_friend')

    def __str__(self) -> str:
        return "{} - {}".format(self.client.name, self.friend.name)