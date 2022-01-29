from rest_framework import mixins, viewsets

from restaurant.menu.models import MenuItem
from restaurant.menu.serializers import MenuItemSerializer


class MenuItemViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
