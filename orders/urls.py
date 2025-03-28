from django.urls import path
from .views import create_order, order_list, order_success


urlpatterns = [
    path("create/", create_order, name="create_order"),
    path("success/<int:order_id>", order_success, name="order_success"),
    path("list/", order_list, name="order_list")
]
