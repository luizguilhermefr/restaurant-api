from rest_framework import routers

from restaurant.menu.views import MenuItemViewSet, OrderViewSet

app_name = "menu"

router = routers.SimpleRouter()

router.register(r"items", MenuItemViewSet, basename="items")
router.register(r"orders", OrderViewSet, basename="orders")

urlpatterns = [
    # ...
]

urlpatterns += router.urls
