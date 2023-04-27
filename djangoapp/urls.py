from django.urls import path
from .tables.bank import views_bank
from .tables.billing import views_billing
from .tables.cards import views_card
from .tables.friend import views_friends
from .tables.personal import views_personal
from .tables.transfer import views_transfer



urlpatterns = [
    ## Users
    path('_persons', views_personal.getPersonals),
    path('create_person', views_personal.addPersonal), 
    path('read_person/<str:pk>', views_personal.getPersonal),
    path('update_person/<str:pk>', views_personal.updatePersonal),
    path('delete_person/<str:pk>', views_personal.deletePersonal), 

    ## Friends
    path('_friends', views_friends.getFriends),
    path('create_friend', views_friends.addFriend), 
    path('read_friend/<str:pk>', views_friends.getFriend),
    path('update_friend/<str:pk>', views_friends.updateFriend),
    path('delete_friend/<str:pk>', views_friends.deleteFriend),     

    ## Cards
    path('_cards', views_card.getCards),
    path('create_card', views_card.addCard), 
    path('read_card/<str:pk>', views_card.getCard),
    path('update_card/<str:pk>', views_card.updateCard),
    path('delete_card/<str:pk>', views_card.deleteCard),

    ## billing
    path('_billing', views_billing.getBillingCards),
    path('create_billing', views_billing.addBillingCard), 
    path('read_billing/<str:pk>', views_billing.getBillingCard),
    path('update_billing/<str:pk>', views_billing.updateBillingCard),
    path('delete_billing/<str:pk>', views_billing.deleteBillingCard),

    ## transfer
    path('_transfer', views_transfer.getTransfers),
    path('create_transfer', views_transfer.addTransfer), 
    path('read_transfer/<str:pk>', views_transfer.getTransfer),
    path('update_transfer/<str:pk>', views_transfer.updateTransfer),
    path('delete_transfer/<str:pk>', views_transfer.deleteTransfer),      

    ## bank
    path('_bank', views_bank.getBankStatements),
    path('create_bank', views_bank.addBankStatement), 
    path('read_bank/<str:pk>', views_bank.getBankStatement),
    path('update_bank/<str:pk>', views_bank.updateBankStatement),
    path('delete_bank/<str:pk>', views_bank.deleteBankStatement),           

]
