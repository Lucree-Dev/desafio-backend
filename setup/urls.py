from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from digital_account_api.views import friend_viewset_post, friend_viewset, get_card_viewset, person_viewset, post_card_viewset, transfer_bankstatement, transfer_bankstatement_user, transfer_viewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('friendpost', friend_viewset_post, basename='friendpost')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls) ),
    path('person/', person_viewset.as_view()),
    path('account/<pk>/friends', friend_viewset.as_view()),
    path('card/', post_card_viewset.as_view()),
    path('account/<pk>/cards', get_card_viewset.as_view()),
    path('transfer/', transfer_viewset.as_view()),
    path('bankstatement/', transfer_bankstatement.as_view()),
    path('bankstatement/<pk>', transfer_bankstatement_user.as_view()),
]
