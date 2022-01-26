from rest_framework import routers

from restaurant.menu.views import MenuItemViewSet

app_name = "menu"

router = routers.SimpleRouter()

router.register(r"items", MenuItemViewSet, basename="items")

urlpatterns = [
    # ...
]

urlpatterns += router.urls
