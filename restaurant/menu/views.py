from rest_framework import mixins, viewsets

from restaurant.menu.models import MenuItem, Order
from restaurant.menu.serializers import MenuItemSerializer, OrderSerializer


class MenuItemViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()


class OrderViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
