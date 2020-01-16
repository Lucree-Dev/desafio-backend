from django.db import models

# Create your models here.
class person(models.Model):
    class Meta:

        db_table = 'user'
    
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=30)
    birthday = models.CharField(max_length=8)
    password = models.CharField(max_length=12)
    username = models.CharField(max_length=20)
    user_id = models.CharField(max_length=40)

    def __str__(self):
        return self.username

class friends(models.Model):
    class Meta:

        db_table = 'friends'

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=30)
    birthday = models.CharField(max_length=8)
    username = models.CharField(max_length=20)
    user_id = models.CharField(max_length=40)

class card(models.Model):
    class Meta:

        db_table = 'card'
    
    card_id = models.CharField(max_length=40)
    title = models.CharField(max_length=10)
    pan = models.CharField(max_length=16)
    expiry_mm = models.CharField(max_length=2)
    expiry_yyyy = models.CharField(max_length=4)
    security_code = models.CharField(max_length=3)
    date = models.CharField(max_length=10)

class cards(models.Model):
    class Meta:

        db_table = 'cards'

    title = models.CharField(max_length=10)
    pan = models.CharField(max_length=16)
    expiry_mm = models.CharField(max_length=2)
    expiry_yyyy = models.CharField(max_length=4)
    security_code = models.CharField(max_length=3)
    date = models.DateField()

class transfer(models.Model):
    class Meta:

        db_table = 'transfer'

    friend_id = models.CharField(max_length=40)
    total_to_transfer = models.IntegerField()
    #billing_card = models.ForeignKey('card', related_name='card_id')

class bank_statement(models.Model):
    class Meta:

        db_table = 'bank_statement'
    
    user_id = models.CharField(max_length=40)
    friend_id = models.CharField(max_length=40)
    value = models.IntegerField()
    date = models.DateField()
    #from_card = models.ForeignKey('card', related_name='card_id')

