from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from cards.api.serializers import CardSerializer
from cards.models import Card, ClientCard
from clients.models import Client

class CreateCardViewset(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )
    http_method_names = [ "post" ]
    serializer_class = CardSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(request.data)
            body = serializer.data

            card = Card.objects.create(
                title = body["title"],
                pan = body["pan"],
                expiry_mm = body["expiry_mm"],
                expiry_yyyy = body["expiry_yyyy"],
                security_code = body["security_code"]
            )
            client = Client.objects.get(user__exact=request.user)
            card_client = ClientCard.objects.create(card=card, client=client)

            return Response({"message": "Cartão cadastrado com sucesso."}, status=201)
        except Exception as e:
            return Response({"message": "Não foi possível cadastrar o cartão."}, status=500)


class ListCardsViewset(ListAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )
    http_method_names = [ "post" ]

    def list(self, request, *args, **kwargs):
        pass