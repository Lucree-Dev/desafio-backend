from django.urls import path
from .views import CreateCardView, ListCardsView

urlpatterns = [
    path('card/', CreateCardView.as_view(), name='add-card'),
    path('cards/', ListCardsView.as_view(), name='list-cards'),
]