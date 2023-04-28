from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('personal/', include('djangoapp.urls')),
    path('friend/', include('djangoapp.urls')),
    path('card/', include('djangoapp.urls')),
    path('transfer/', include('djangoapp.urls')),
    path('billing/', include('djangoapp.urls')),
    path('bank/', include('djangoapp.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name="schema"))
]