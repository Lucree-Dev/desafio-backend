from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from clients.models import Client
from .serializers import CardSerializer
from .models import Card, BillingCard


class CreateCardView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    http_method_names = ['post']
    serializer_class = CardSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(request.data)
            data = serializer.data
            card = Card.objects.create(
                title=data['title'],
                pan=data['pan'],
                expiry_mm=data['expiry_mm'],
                expiry_yyyy=data['expiry_yyyy'],
                security_code=data['security_code'],
                card_id=data['card_id'],
            )
            client = Client.objects.get(user__exact=request.user)
            billing_card = BillingCard.objects.create(card=card, client=client)

            return Response({'message': 'Card created.'}, status=201)
        except Exception as e:
            return Response({'message': 'Card creation error.'}, status=500)


class ListCardsView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        client = Client.objects.get(user__exact=request.user)

        queryset = BillingCard.objects.filter(client__exact=client)
        cards = list(map(lambda x: x.card, queryset))
        serializer = CardSerializer(cards, many=True)

        return Response(serializer.data, status=200)
