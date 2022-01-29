from rest_framework import serializers

from restaurant.menu.models import MenuItem


class MenuItemSerializer(serializers.Serializer):
    class Meta:
        model = MenuItem