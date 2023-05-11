from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from clients.models import Client, ClientFriend
from .serializers import CreateClientSerializer, AddFriendSerializer, ClientSerializer


class CreateClientView(CreateAPIView):
    serializer_class = CreateClientSerializer
    http_method_names = ['post']
    _user_model = get_user_model()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)

        serializer.is_valid(raise_exception=True)

        user_exists = self.__user_exists(data)
        if user_exists:
            return Response(data={'message': 'User exists.'}, status=400)

        user = self.__create_user(data)

        client = Client.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            birthday=datetime.strptime(data['birthday'], '%Y-%m-%d'),
            user=user
        )
        client.save()

        return Response(data={'message': 'Client created.'}, status=201)

    def __user_exists(self, data):
        query = self._user_model.objects.filter(Q(email=data['email']) | Q(email=data['username'])).first()
        return bool(query)

    def __create_user(self, data):
        password = make_password(data['password'])

        query = self._user_model.objects.create(
            email=data['email'],
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            password=password
        )
        query.set_password(password)
        return query


class ClientFriendsView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    http_method_names = ['get']

    def get(self, request):
        try:
            client = Client.objects.get(user=request.user)
        except Exception as e:
            return Response('Client not found', status=404)

        friend_list = []

        queryset = ClientFriend.objects.filter(Q(client__exact=client) | Q(friend__exact=client))
        for item in queryset:
            friend = item.friend if item.client == client else item.client
            friend_list.append(friend)

        serializer = ClientSerializer(friend_list, many=True)

        return Response(serializer.data, status=200)
