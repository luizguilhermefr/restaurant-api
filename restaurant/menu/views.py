from rest_framework import mixins, status, viewsets

from restaurant.menu.models import MenuItem


class MenuItemViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    model = MenuItem
    permission_classes = ()
    authentication_classes = ()
