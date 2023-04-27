from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('personal/', include('djangoapp.urls')),
    path('friend/', include('djangoapp.urls')),
    path('card/', include('djangoapp.urls')),
    path('transfer/', include('djangoapp.urls')),
    path('billing/', include('djangoapp.urls')),
    path('bank/', include('djangoapp.urls')),
]