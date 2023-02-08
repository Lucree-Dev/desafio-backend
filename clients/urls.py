from django.urls import path
from clients.models import Client
from clients.api.viewsets import CreateClientViewset, ClientFriendsViewset

urlpatterns = [
    path("person/", CreateClientViewset.as_view(), name="add-client"),
    path("friends/", ClientFriendsViewset.as_view(), name="friends")
]