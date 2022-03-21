from django.urls import path
from . import views

urlpatterns = [
    path('verifications', views.verifications),
    path('verify/<customer_id>', views.verify),
    path('check_ipx', views.check_ip)
]