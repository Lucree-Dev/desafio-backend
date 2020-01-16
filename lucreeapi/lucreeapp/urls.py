from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^card/$', views.CardList.as_view(), name='card-list'),

]