from rest_framework import serializers

from restaurant.menu.models import MenuItem, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("src",)


class MenuItemSerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = MenuItem
        fields = ("id", "name", "price", "image")
