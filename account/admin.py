from django.contrib import admin
from account.models import Person
from account.models import Friend
from account.models import Card
from account.models import Transfer


class Persons(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name', 'birthday', 'password', 'username')
    list_display_links = ('user_id', 'first_name')
    list_per_page = 10

admin.site.register(Person, Persons)

class Friends(admin.ModelAdmin):
    list_display = ('friend_id', 'first_name', 'last_name', 'birthday', 'username', 'user_id')
    list_display_links = ('first_name', 'username')
    list_per_page = 10

admin.site.register(Friend, Friends)


class Cards(admin.ModelAdmin):
    list_display = ('card_id', 'title', 'pan', 'expiry_mm', 'expiry_yyyy', 'security_code', 'date')
    list_display_links = ('card_id', 'title')
    list_per_page = 10

admin.site.register(Card, Cards)


class Transfers(admin.ModelAdmin):
    list_display = ('friend_id', 'total_to_transfer', 'billing_card')
    list_display_links = ('friend_id',)
    list_per_page = 15

admin.site.register(Transfer, Transfers)


