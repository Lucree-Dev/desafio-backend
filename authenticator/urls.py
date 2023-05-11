from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='get_token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh_token')
]
