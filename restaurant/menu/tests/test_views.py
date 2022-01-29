import pytest
from django.urls import reverse
from rest_framework import status

from restaurant.menu.tests.factories import MenuItemFactory

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
