from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import datetime


class Person(User, AbstractUser):
    user_id = models.CharField(max_length=40, null=False, primary_key=True, blank=False)
    birthday = models.CharField(max_length=10, null=False, blank=False)


class Friend(models.Model):
    user_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    friend_id = models.CharField(max_length=40, primary_key=True)
    first_name = models.CharField(max_length=15, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birthday = models.CharField(max_length=10, null=False)
    username = models.CharField(max_length=15, null=False)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Card(models.Model):
    card_id = models.CharField(max_length=40, null=False, primary_key=True)
    title = models.CharField(max_length=10, null=False)
    pan = models.CharField(max_length=20, null=False)
    expiry_mm = models.CharField(max_length=2, null=False)
    expiry_yyyy = models.CharField(max_length=4, null=False)
    security_code = models.CharField(max_length=3, null=False)
    date = models.CharField(max_length=10, null=False)

    def __str__(self) -> str:
        return f'{self.title}[{self.card_id}]'


class Transfer(models.Model):
    friend_id = models.ForeignKey(Friend, on_delete=models.CASCADE)
    billing_card = models.ForeignKey(Card, on_delete=models.CASCADE)
    total_to_transfer = models.IntegerField(null=False)
    date = models.CharField(max_length=10, default=str(datetime.date.today().strftime('%m/%d/%Y')))

