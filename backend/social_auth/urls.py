from rest_framework.routers import SimpleRouter

from django.urls import include
from django.urls import path

from social_auth.api.viewsets import exchange_token

urlpatterns = [
    path('<str:backend>/', exchange_token),
]
