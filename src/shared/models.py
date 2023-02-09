from django.db import models
from django.utils import timezone
from model_utils.models import SoftDeletableModel
import uuid

class BaseModel(SoftDeletableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now())

    @property
    def date(self):
        created_at = self.created_at
        return "{}/{}/{}".format(str(created_at.day).rjust(2, "0"), str(created_at.month).ljust(2, "0"), created_at.year)

    class Meta:
        abstract = True