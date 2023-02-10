from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from account.models import Person
from account.models import Friend
from account.models import Card
from account.models import Transfer


class AccountPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birthday', 'password', 'username', 'user_id']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['email'] = validated_data['username']
        return super(AccountPersonSerializer, self).create(validated_data)


class AccountFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ['first_name', 'last_name', 'birthday', 'username', 'user_id']

class AccountCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['card_id', 'title', 'pan', 'expiry_mm', 'expiry_yyyy', 'security_code', 'date']


class AccountCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['title', 'pan', 'expiry_mm', 'expiry_yyyy', 'security_code', 'date']


class AccountTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['friend_id', 'total_to_transfer', 'billing_card']


class AccountBankStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['friend_id', 'total_to_transfer', 'date', 'billing_card']



class AccountBankStatementUserIDListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['friend_id', 'total_to_transfer', 'date', 'billing_card']
