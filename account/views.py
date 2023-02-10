from rest_framework import viewsets
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from account.models import Person
from account.models import Card
from account.models import  Transfer
from account.models import Friend
from account.serializer import AccountPersonSerializer
from account.serializer import AccountFriendsSerializer
from account.serializer import AccountCardSerializer
from account.serializer import AccountCardsSerializer
from account.serializer import AccountTransferSerializer
from account.serializer import AccountBankStatementSerializer
from account.serializer import AccountBankStatementUserIDListSerializer


class AccountPersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = AccountPersonSerializer
    http_method_names = ['post']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AccountFriendsViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = AccountFriendsSerializer
    http_method_names = ['get']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AccountCardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = AccountCardSerializer
    http_method_names = ['post']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AccountCardsViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = AccountCardsSerializer
    http_method_names = ['get']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AccountTransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = AccountTransferSerializer
    http_method_names = ['post']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AccountBankStatementViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = AccountBankStatementSerializer
    http_method_names = ['get']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AccountBankStatementUserIDList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Transfer.objects.filter(friend_id=self.kwargs['usertID'])
        return queryset
        
    serializer_class = AccountBankStatementUserIDListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]