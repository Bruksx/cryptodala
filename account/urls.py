from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('modify', views.modify),
    path('logout', views.logout),
    path('verify', views.verify),
]