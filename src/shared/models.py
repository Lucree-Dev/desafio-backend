from django.db import models
from django.utils import timezone
from model_utils.models import SoftDeletableModel
import uuid

class BaseModel(SoftDeletableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now())

    class Meta:
        abstract = True