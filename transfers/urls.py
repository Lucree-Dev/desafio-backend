from django.urls import path
from .views import TransferView, ListTransfersView

urlpatterns = [
    path('transfer/', TransferView.as_view(), name='transfer'),
    path('bank-statement/', ListTransfersView.as_view({'get': 'list'}), name='list-transfers'),
    path('bank-statement/<str:user_id>/', ListTransfersView.as_view({'get': 'retrieve'}), name='list-transfers-to-friend'),
]