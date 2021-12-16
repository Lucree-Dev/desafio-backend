from rest_framework import serializers
from digital_account_api.models import account, card, friend, transfer
import datetime

class account_serializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = '__all__'

class card_serializer(serializers.ModelSerializer):
    date = serializers.DateField(datetime.datetime.now().date(), read_only = True)
    class Meta:
        model = card
        fields = '__all__'

class person_serializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=20)
    birthday = serializers.DateField()
    password = serializers.CharField(max_length=8)
    username = serializers.CharField(max_length=15)  
    class Meta:
        model = account
        fields = '__all__'
    
   
class friend_serializer(serializers.ModelSerializer):
    friend_first_name = serializers.ReadOnlyField(source="friend_id.first_name")
    friend_last_name = serializers.ReadOnlyField(source="friend_id.last_name")
    friend_birthday = serializers.ReadOnlyField(source="friend_id.birthday")
    friend_username = serializers.ReadOnlyField(source="friend_id.username")
    class Meta:
        model = friend
        fields = ['friendship_id','user_id', 'friend_id', 'friend_first_name', 'friend_last_name', 'friend_birthday', 'friend_username']

class post_card_serializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=30)
    pan = serializers.CharField(max_length=16)
    expiry_mm = serializers.CharField(max_length=2)
    expiry_yyyy = serializers.CharField(max_length=4)
    security_code = serializers.CharField(max_length=4)
    date = serializers.DateField(datetime.datetime.now().date(), read_only = True) 
    class Meta:
        model = card
        fields = '__all__'

class get_card_serializer(serializers.ModelSerializer):
    class Meta:
        model = card
        exclude = ['user_id', 'card_id']

class transfer_serializer(serializers.ModelSerializer):
    total_to_pay = serializers.IntegerField()
    class Meta:
        model = transfer
        fields = ['user_id', 'transfer_id', 'friendship_id', 'total_to_pay', 'billing_card']