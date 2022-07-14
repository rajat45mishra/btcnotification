from django.db import models

# Create your models here.


class NotificationPrice(models.Model):
    name = models.CharField(max_length=100, default="")
    NotificationPrice = models.IntegerField()
    email = models.EmailField(default="r@R.COM")
