from rest_framework import serializers

from restaurant.menu.models import MenuItem


class OrderMenuItemField(serializers.RelatedField):
    queryset = MenuItem.objects.all()

    def to_representation(self, obj):
        return {"id": obj.pk, "name": obj.name}

    def to_internal_value(self, value):
        return self.queryset.get(pk=value)

    def run_validation(self, value):
        if self.queryset.filter(pk=value).first() == None:
            raise serializers.ValidationError("Item does not exist.")

        return super().run_validation(value)
