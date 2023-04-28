from django.db import models

## Usuario
class Personal(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birthday = models.CharField(max_length=10)
    password = models.CharField(max_length=150)
    username = models.CharField(max_length=300)
    user_id = models.CharField(max_length=1000)


class Friend(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birthday = models.CharField(max_length=10)
    username = models.CharField(max_length=300)
    user_id = models.CharField(max_length=1000)

class Card(models.Model):
    card_id = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    pan = models.CharField(max_length=40)
    expiry_mm = models.CharField(max_length=2)
    expiry_yyyy = models.CharField(max_length=4)  
    security_code = models.CharField(max_length=3)
    date = models.CharField(max_length=10)

class Transfer(models.Model):
    friend_id = models.CharField(max_length=150)
    total_to_transfer = models.IntegerField(max_length=5)

class BillingCard(models.Model):
    card_id = models.CharField(max_length=1000)


class BankStatement(models.Model):
    user_id = models.CharField(max_length=1000)
    friend_id = models.CharField(max_length=1000)
    value = models.IntegerField(max_length=100)
    date = models.CharField(max_length=1000)
    from_card = models.CharField(max_length=1000)

