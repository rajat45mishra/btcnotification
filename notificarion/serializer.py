from rest_framework import serializers
from .models import NotificationPrice


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationPrice
        fields = "__all__"
