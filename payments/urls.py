from django.urls import path, include
from payments.api.viewsets import TransferViewset, ListTransfersViewset

urlpatterns = [
    path("transfer/", TransferViewset.as_view(), name="transfer"),
    path("bank-statement/", ListTransfersViewset.as_view({'get': 'list'}), name="list-transfers"),
    path("bank-statement/<str:id>/", ListTransfersViewset.as_view({'get': 'retrieve'}), name="list-transfers-to-friend"),
]