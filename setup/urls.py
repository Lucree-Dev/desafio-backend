from django.contrib import admin
from django.urls import path
from django.urls import include
from account.views import AccountPersonViewSet
from account.views import AccountFriendsViewSet
from account.views import AccountCardViewSet
from account.views import AccountCardsViewSet
from account.views import AccountTransferViewSet
from account.views import AccountBankStatementViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('account/person', AccountPersonViewSet, basename='Persons')
router.register('account/friends', AccountFriendsViewSet, basename='Friends')
router.register('account/card', AccountCardViewSet, basename='Card')
router.register('account/cards', AccountCardsViewSet, basename='Cards')
router.register('account/transfer', AccountTransferViewSet, basename='Transfer')
router.register('account/bank-statement', AccountBankStatementViewSet, basename='Bank Statement')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('account/bank-statement<int:usertID>/', AccountBankStatementViewSet.as_view({'get': 'list'}))
]
