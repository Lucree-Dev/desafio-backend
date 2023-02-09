from django.urls import path
from cards.api.viewsets import CreateCardViewset, ListCardsViewset

urlpatterns = [
    path("card/", CreateCardViewset.as_view(), name="add-card"),
    path("cards/", ListCardsViewset.as_view(), name="list-cards"),
]