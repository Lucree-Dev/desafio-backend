from django.urls import path
from clients.models import Client
from clients.api.viewsets import CreateClientViewset

urlpatterns = [
    path("person/", CreateClientViewset.as_view(), name="add-client")
]