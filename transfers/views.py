from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .serializers import CreateTransferSerializer, ListTransfersSerializer
from .models import Transfer
from cards.models import BillingCard
from clients.models import Client


class TransferView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    http_method_names = ['post']
    serializer_class = CreateTransferSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(request.data)
            data = serializer.data
            card_id = data['billing_card']['card_id']
            client = Client.objects.get(user__exact=request.user)
            billing_card = BillingCard.objects.filter(client=client, card_id=card_id).first()

            if billing_card.client != client:
                return Response({'message': 'Wrong card number.'}, status=403)

            friend = Client.objects.get(id=data['friend_id'])
            if friend is None:
                return Response({'message': 'User not found.'}, status=400)
            transfer = Transfer.objects.create(
                friend=friend,
                total_to_pay=int(data['total_to_pay']),
                billing_card=billing_card,
            )

            return Response({'message': 'Transfer success.'}, status=201)
        except Exception as e:
            return Response({'message': 'Transfer Error.'}, status=500)


class ListTransfersView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    http_method_names = ['get']
    serializer_class = ListTransfersSerializer

    def list(self, request, *args, **kwargs):
        transfers = self.__get_transfers(request.user)
        serializer = self.get_serializer(transfers, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, user_id):
        transfers = self.__get_transfers(request.user)

        if user_id:
            transfers = transfers.filter(friend__id=user_id)

        serializer = self.get_serializer(transfers, many=True)
        return Response(serializer.data, status=200)

    def __get_transfers(self, user):
        client = Client.objects.filter(user__exact=user).first()
        transfers = Transfer.objects.filter(billing_card__client__exact=client)
        return transfers