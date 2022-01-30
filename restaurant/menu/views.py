from rest_framework import mixins, viewsets

from restaurant.menu.models import MenuItem, Order
from restaurant.menu.serializers import (
    MenuItemSerializer,
    OrderWriteSerializer,
    OrderListSerializer,
)


class MenuItemViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()


class OrderViewSet(
    viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin
):
    permission_classes = ()
    authentication_classes = ()
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return OrderWriteSerializer

        return OrderListSerializer
