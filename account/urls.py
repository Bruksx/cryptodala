from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('modify', views.modify),
    path('logout', views.logout),
    path('verify', views.verify),
    path('add_address', views.add_address),
    path('get_address', views.get_address),
]