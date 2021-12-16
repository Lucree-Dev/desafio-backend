from rest_framework import viewsets, generics
from digital_account_api.models import account, card, friend, transfer
from digital_account_api.serializers import account_serializer, card_serializer, friend_serializer, get_card_serializer, person_serializer, post_card_serializer, transfer_serializer
from rest_framework.permissions import IsAuthenticated
class friend_viewset_post(viewsets.ModelViewSet):
     """Feita pra postar os amigos do usuário"""
     permission_classes = (IsAuthenticated, )
     queryset = friend.objects.all()
     serializer_class = friend_serializer

class person_viewset(generics.CreateAPIView):
     """Cria um novo usuário"""
     permission_classes = (IsAuthenticated, )
     def perform_create(self, serializer):
      return serializer.save()
     serializer_class = person_serializer

class post_card_viewset(generics.CreateAPIView):
     """Cria um novo cartão"""
     permission_classes = (IsAuthenticated, )
     def perform_create(self, serializer):
      return serializer.save()
     serializer_class = post_card_serializer

class friend_viewset(generics.ListAPIView):
     """Exibir os amigos do usuario"""
     permission_classes = (IsAuthenticated, )
     def get_queryset(self):
        queryset = friend.objects.filter(user_id=self.kwargs['pk'])
        return queryset
     serializer_class = friend_serializer

class get_card_viewset(generics.ListAPIView):
     """Exibir os amigos do usuario"""
     permission_classes = (IsAuthenticated, )
     def get_queryset(self):
        queryset = card.objects.filter(user_id=self.kwargs['pk'])
        return queryset
     serializer_class = get_card_serializer

class post_card_viewset(generics.CreateAPIView):
     """Realiza transfêrencia entre amigos"""
     permission_classes = (IsAuthenticated, )
     def perform_create(self, serializer):
      return serializer.save()
     serializer_class = post_card_serializer

class transfer_viewset(generics.CreateAPIView):
     """Realiza transferências com os amigos do usuário"""
     permission_classes = (IsAuthenticated, )
     def perform_create(self, serializer):    
      return serializer.save()
     serializer_class = transfer_serializer

class transfer_bankstatement(generics.ListAPIView):
     permission_classes = (IsAuthenticated, )
     def get_queryset(self):
        queryset = transfer.objects.all()
        return queryset
     serializer_class = transfer_serializer

class transfer_bankstatement_user(generics.ListAPIView):
     permission_classes = (IsAuthenticated, )
     def get_queryset(self):
        queryset = transfer.objects.filter(user_id=self.kwargs['pk'])
        return queryset
     serializer_class = transfer_serializer