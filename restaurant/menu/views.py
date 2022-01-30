from rest_framework import mixins, viewsets

from restaurant.menu.models import MenuItem, Order
from restaurant.menu.serializers import (
    MenuItemSerializer,
    OrderWriteSerializer,
    OrderListSerializer,
)
from restaurant.utils import CsrfExemptSessionAuthentication


class BaseViewSet(viewsets.GenericViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication,)


class MenuItemViewSet(BaseViewSet, mixins.ListModelMixin):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()


class OrderViewSet(BaseViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    permission_classes = ()
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return OrderWriteSerializer

        return OrderListSerializer
