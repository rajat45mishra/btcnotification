from django.shortcuts import render
from notificarion.models import NotificationPrice
from .serializer import NotificationSerializer

# Create your views here.
from rest_framework import viewsets


class TestClass(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = NotificationPrice.objects.all()
