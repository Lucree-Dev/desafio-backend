from django.urls import path
from authentication.api.viewsets import LoginViewset
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    path("login/", LoginViewset.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh')
]