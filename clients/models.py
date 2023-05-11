from django.db import models
from django.conf import settings
from django.utils import timezone

class Client(models.Model):
    first_name = models.CharField(max_length=40, blank=False, null=False, default="")
    last_name = models.CharField(max_length=90, blank=False, null=False, default="")
    birthday = models.DateField(default=timezone.now())
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False, default="")

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class ClientFriend(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='%(class)s_client')
    friend = models.ForeignKey(Client, on_delete=models.CASCADE,  related_name='%(class)s_friend')

    def __repr__(self) -> str:
        return f"{self.client} - {self.friend}"

    def __str__(self) -> str:
        return f"{self.client} - {self.friend}"
