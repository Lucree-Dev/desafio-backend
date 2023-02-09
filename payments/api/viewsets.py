from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.db.models import Q
from payments.api.serializers import CreateTransferSerializer, ListTransfersSerializer
from payments.models import Transfers
from cards.models import ClientCard
from clients.models import Client


class TransferViewset(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )
    http_method_names = [ "post" ]
    serializer_class = CreateTransferSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(request.data)
            body = serializer.data

            card_id = body["billing_card"]["card_id"]
            client = Client.objects.get(user__exact=request.user)
            client_card = ClientCard.objects.filter(client__exact=client, card__id=card_id).first()

            if client_card.client != client:
                return Response({"message": "Cartão informado inválido."}, status=403)

            friend = Client.objects.filter(id=body["friend_id"]).first()
            if friend is None:
                return Response({"message": "Usuário informado não encontrado."}, status=400)

            transfer = Transfers.objects.create(
                friend = friend,
                total_to_transfer = body["total_to_transfer"],
                client_card = client_card
            )

            return Response({"message": "Transferência realizada com sucesso."}, status=201)
        except Exception as e:
            return Response({"message": "Não foi possível realizar a transferência."}, status=500)


            
class ListTransfersViewset(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )
    http_method_names = [ "get" ]
    serializer_class = ListTransfersSerializer

    def list(self, request, *args, **kwargs):
        transfers = self.__get_transfers(request.user)
        serializer = self.get_serializer(transfers, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, id):
        transfers = self.__get_transfers(request.user)

        if id:
            transfers = transfers.filter(friend__id=id)

        serializer = self.get_serializer(transfers, many=True)
        return Response(serializer.data, status=200)

    def __get_transfers(self, user):
        client = Client.objects.filter(user__exact=user).first()
        transfers = Transfers.objects.filter(client_card__client__exact=client)
        return transfers