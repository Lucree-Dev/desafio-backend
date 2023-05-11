from django.urls import path, include
from .views import CreateClientView, ClientFriendsView


urlpatterns = [
    path('person/', CreateClientView.as_view(), name='add-client'),
    path('friends/', ClientFriendsView.as_view(), name='friends'),
    path('', include('cards.urls')),
    path('', include('transfers.urls'))
]