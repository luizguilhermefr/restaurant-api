import re
import uuid

from django.db import transaction
from rest_framework import serializers

from restaurant.menu.fields import OrderMenuItemField
from restaurant.menu.models import MenuItem, Image, Order, OrderItem, Payment


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("src",)


class MenuItemSerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = MenuItem
        fields = ("id", "name", "price", "image")


class OrderItemSerializer(serializers.ModelSerializer):
    item = OrderMenuItemField()
    price = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2)

    class Meta:
        model = OrderItem
        fields = ("item", "quantity", "price")


class OrderWriteSerializer(serializers.ModelSerializer):
    credit_card_number = serializers.CharField(
        min_length=16, max_length=16, write_only=True
    )
    credit_card_cvv = serializers.CharField(min_length=3, max_length=3, write_only=True)
    credit_card_exp_date = serializers.CharField(
        min_length=5, max_length=5, write_only=True
    )
    items = serializers.ListField(
        child=OrderItemSerializer(), min_length=1, write_only=True
    )
    confirmation = serializers.UUIDField(source="payment.confirmation", read_only=True)

    def validate_credit_card_number(self, value):
        p = re.compile(
            "^5[1-5][0-9]{14}|^(222[1-9]|22[3-9]\\d|2[3-6]\\d{2}|27[0-1]\\d|2720)[0-9]{12}$"
        )

        if not (re.search(p, value)):
            raise serializers.ValidationError("Credit card number is invalid.")

        return value

    def validate_credit_card_exp_date(self, value):
        p = re.compile("^(0[1-9]|1[0-2])/?([0-9]{4}|[0-9]{2})$")

        if not (re.search(p, value)):
            raise serializers.ValidationError("Expiration date is invalid.")

        return value

    def validate_credit_card_cvv(self, value):
        p = re.compile("^[0-9]{3}$")

        if not (re.search(p, value)):
            raise serializers.ValidationError("CVV is invalid.")

        return value

    @transaction.atomic
    def create(self, validated_data):
        payment = Payment.objects.create(
            confirmation=uuid.uuid4()  # This would be probably the return of a payment processor system, such as Stripe
        )
        order = Order.objects.create(payment=payment)
        for item in validated_data["items"]:
            OrderItem.objects.create(
                order=order,
                quantity=item["quantity"],
                item=item["item"],
                price=item["item"].price,
            )

        return order

    class Meta:
        model = Order
        fields = (
            "credit_card_number",
            "credit_card_cvv",
            "credit_card_exp_date",
            "items",
            "confirmation",
        )


class OrderListSerializer(serializers.ModelSerializer):
    payment_confirmation = serializers.UUIDField(
        source="payment.confirmation", allow_null=True
    )
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "created_at",
            "payment_confirmation",
            "total",
            "items",
        )
