from rest_framework.generics import CreateAPIView
from clients.api.serializers import ClientSerializer
from django.contrib.auth import get_user_model
from django.db.models import Q
from clients.models import Client
from rest_framework.response import Response
from datetime import datetime

class CreateClientViewset(CreateAPIView):
    serializer_class = ClientSerializer
    http_method_names = [ "post" ]
    _user_model = get_user_model()

    def __user_exists(self, body):
        query = self._user_model.objects.filter(Q(email=body["email"]) | Q(email=body["username"])).first()
        return bool(query)

    def __create_user(self, body):
        query = self._user_model.objects.create(
            email = body["email"],
            username = body["username"],
            first_name = body["first_name"],
            last_name = body["last_name"]
        )
      
        query.set_password(body["password"])
        return query.pk


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