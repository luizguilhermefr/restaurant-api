import json

import pytest
from django.urls import reverse
from rest_framework import status

from restaurant.menu.models import Order, OrderItem
from restaurant.menu.tests.factories import (
    MenuItemFactory,
    OrderItemFactory,
)

pytestmark = pytest.mark.django_db


class TestMenuItemViewSet:
    @pytest.fixture
    def url(self):
        return reverse("menu:items-list")

    @pytest.fixture
    def items(self):
        return MenuItemFactory.create_batch(5)

    def test_returns_items_along_with_images(self, url, client, items):
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) > 0
        fields_to_expect = ("id", "name", "price", "image")
        for item in response.data:
            assert all(field in item for field in fields_to_expect)


class TestOrderViewSet:
    @pytest.fixture
    def url(self):
        return reverse("menu:orders-list")

    def test_creates_an_order(self, url, client):
        cake = MenuItemFactory.create(name="cake")
        coffee = MenuItemFactory.create(name="coffee")
        post_data = json.dumps(
            {
                "credit_card_number": "5376788249899522",
                "credit_card_cvv": "445",
                "credit_card_exp_date": "05/28",
                "items": [
                    {"item": coffee.id, "quantity": 2},
                    {"item": cake.id, "quantity": 1},
                ],
            }
        )

        response = client.post(url, data=post_data, content_type="application/json")
        assert response.status_code == status.HTTP_201_CREATED
        orders = Order.objects.all()
        assert len(orders) == 1
        items = OrderItem.objects.filter(order=orders[0]).all()
        assert len(items) == 2
        assert items[0].quantity == 2
        assert items[0].item == coffee
        assert items[1].quantity == 1
        assert items[1].item == cake

    def test_validates_inexistent_product(self, url, client):
        post_data = json.dumps(
            {
                "credit_card_number": "5376788249899522",
                "credit_card_cvv": "445",
                "credit_card_exp_date": "05/28",
                "items": [
                    {"item": 12345566, "quantity": 1},
                ],
            }
        )

        response = client.post(url, data=post_data, content_type="application/json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {"items": {0: {"item": ["Item does not exist."]}}}

    @pytest.mark.parametrize(
        "credit_card_number,error_expected",
        (
            ("invalid", "Ensure this field has at least 16 characters."),
            ("invalidinvalidinva", "Ensure this field has no more than 16 characters."),
            ("9999788249899522", "Credit card number is invalid."),
        ),
    )
    def test_validates_invalid_credit_card_number(
        self, url, client, credit_card_number, error_expected
    ):
        product = MenuItemFactory.create()

        post_data = json.dumps(
            {
                "credit_card_number": credit_card_number,
                "credit_card_cvv": "445",
                "credit_card_exp_date": "05/28",
                "items": [
                    {"item": product.id, "quantity": 1},
                ],
            }
        )

        response = client.post(url, data=post_data, content_type="application/json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {"credit_card_number": [error_expected]}

    @pytest.mark.parametrize(
        "credit_card_exp_date,error_expected",
        (
            ("12", "Ensure this field has at least 5 characters."),
            ("invalid", "Ensure this field has no more than 5 characters."),
            ("12+23", "Expiration date is invalid."),
        ),
    )
    def test_validates_invalid_credit_card_exp_date(
        self, url, client, credit_card_exp_date, error_expected
    ):
        product = MenuItemFactory.create()

        post_data = json.dumps(
            {
                "credit_card_number": "5376788249899522",
                "credit_card_cvv": "445",
                "credit_card_exp_date": credit_card_exp_date,
                "items": [
                    {"item": product.id, "quantity": 1},
                ],
            }
        )

        response = client.post(url, data=post_data, content_type="application/json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {"credit_card_exp_date": [error_expected]}

    @pytest.mark.parametrize(
        "credit_card_cvv,error_expected",
        (
            ("12", "Ensure this field has at least 3 characters."),
            ("invalid", "Ensure this field has no more than 3 characters."),
            ("abc", "CVV is invalid."),
        ),
    )
    def test_validates_invalid_credit_card_exp_date(
        self, url, client, credit_card_cvv, error_expected
    ):
        product = MenuItemFactory.create()

        post_data = json.dumps(
            {
                "credit_card_number": "5376788249899522",
                "credit_card_cvv": credit_card_cvv,
                "credit_card_exp_date": "12/28",
                "items": [
                    {"item": product.id, "quantity": 1},
                ],
            }
        )

        response = client.post(url, data=post_data, content_type="application/json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {"credit_card_cvv": [error_expected]}

    def test_lists_orders(self, url, client):
        OrderItemFactory.create(quantity=2, price=15)
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

        fields_to_expect_orders = (
            "id",
            "created_at",
            "payment_confirmation",
            "total",
            "items",
        )

        for order in response.data:
            assert all(field in order for field in fields_to_expect_orders)
