from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(CreateAPIView):
    def __generate_jwt(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    def create(self, request, *args, **kwargs):
        body = request.data
        user = authenticate(request, username=body['username'], password=body['password'])

        if user:
            token = self.__generate_jwt(user=user)
            return Response({'token': token})

        return Response({'message': 'No user found.'}, status=400)