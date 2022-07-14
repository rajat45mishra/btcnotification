from ast import mod
import re
from celery import shared_task
import requests
from django.db.models import Q
from django.core.mail import send_mail
from notificarion.models import NotificationPrice
import json


@shared_task
def sample_task():
    from notificarion import models

    data = requests.get(
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    )
    data = json.load(data)
    price = 0
    for i in data:
        if i["id"] == "bitcoin":
            price = i["current_price"]
    notfi = models.NotificationPrice.objects.filter(Q(NotificationPrice__lte=price))
    if notfi:
        for i in notfi:
            send_mail(
                f"BTC:${i.NotificationPrice}",
                "comment tu vas?",
                "paul@polo.com",
                [i.email],
            )
