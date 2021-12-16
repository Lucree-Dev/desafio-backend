from django.db import models
from uuid import uuid4
import datetime

from django.db.models.deletion import CASCADE

class account(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    birthday = models.DateField()
    password = models.CharField(max_length=8)
    username = models.CharField(max_length=15) 

    def __str__(self):
        return self.username 


class card(models.Model):
    user_id = models.ForeignKey(account, on_delete=models.CASCADE)
    card_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=30)
    pan = models.CharField(max_length=16)
    expiry_mm = models.CharField(max_length=2)
    expiry_yyyy = models.CharField(max_length=4)
    security_code = models.CharField(max_length=4, default=1234)

    def __str__(self):
      return self.title

class friend(models.Model):
    friendship_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_id = models.ForeignKey(account,on_delete=models.CASCADE, related_name="current_user")
    friend_id  = models.ForeignKey(account,on_delete=models.CASCADE, related_name="user_friend")

class transfer(models.Model):
    transfer_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_id = models.ForeignKey(account, on_delete=models.CASCADE)
    friendship_id = models.ForeignKey(friend, on_delete=models.CASCADE)
    transfer_message = models.CharField(max_length=100)
    total_to_pay = models.IntegerField()
    billing_card = models.ForeignKey(card, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, editable=False)

    def __UUID__(self):
      return self.transfer_id
