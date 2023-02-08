from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date
from model_utils.models import SoftDeletableModel
import uuid


class BaseModel(SoftDeletableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Client(BaseModel):
    name = models.CharField(max_length=30, blank=False, null=False, default="")
    lastname = models.CharField(max_length=70, blank=False, null=False, default="")
    birthday = models.DateField(max_length=date.today(), default=timezone.now())
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False, default="")

    def __str__(self) -> str:
        return "{} {}".format(self.name, self.lastname)
