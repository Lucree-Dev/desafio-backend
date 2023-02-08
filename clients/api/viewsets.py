from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.db.models import Q
from datetime import datetime
from clients.api.serializers import CreateClientSerializer, AddFriendSerializer, ClientSerializer
from clients.models import Client, ClientFriends
from django.contrib.auth.hashers import make_password


class CreateClientViewset(CreateAPIView):
    serializer_class = CreateClientSerializer
    http_method_names = [ "post" ]
    _user_model = get_user_model()

    def create(self, request, *args, **kwargs):
        body = request.data
        serializer = self.get_serializer(data=body)

        serializer.is_valid(raise_exception=True)

        user_exists = self.__user_exists(body)
        if user_exists:
            return Response(data={"message": "Já existe um usuário com este login."}, status=400)

        user_id = self.__create_user(body)

        client = Client.objects.create(
            name = body["first_name"],
            lastname = body["last_name"],
            birthday = datetime.strptime(body["birthday"], "%Y-%m-%d"),
            user_id = user_id
        )
        client.save()

        return Response(data={"message": "Cliente cadastrado com sucesso."}, status=201)
    
    def __user_exists(self, body):
        query = self._user_model.objects.filter(Q(email=body["email"]) | Q(email=body["username"])).first()
        return bool(query)

    def __create_user(self, body):
        password = make_password(body["password"])

        query = self._user_model.objects.create(
            email = body["email"],
            username = body["username"],
            first_name = body["first_name"],
            last_name = body["last_name"],
            password = password
        )     
        query.set_password(password)
        return query.pk


class ClientFriendsViewset(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTAuthentication, )
    http_method_names = [ "get", "post" ]

    def get(self, request):
        client = Client.objects.get(user__exact=request.user)
        friend_list = []

        queryset = ClientFriends.objects.filter(Q(client__exact=client) | Q(friend__exact=client))
        for item in queryset:
            friend = item.friend if item.client == client else item.client
            friend_list.append(friend)

        serializer = ClientSerializer(friend_list, many=True)

        return Response(serializer.data, status=200)

    def post(self, request):
        try:
            client = Client.objects.get(user__id=request.user.id)

            friend_username = request.data["friend_username"]
            friend = Client.objects.filter(user__username__exact = friend_username).first()

            if friend is None:
                return Response({"message": "Nenhum usuário encontrado com este 'username'."}, status=400)

            ClientFriends.objects.create(client=client, friend=friend)
            
            return Response({"message": "Amigo adicionado com sucesso."}, status=201)

        except Exception as e:
            return Response({"message": "Erro com o servidor."}, status=500)