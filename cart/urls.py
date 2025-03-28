from django.urls import path
from .views import cart_view, add_to_cart, update_cart, delete_from_cart

urlpatterns = [
    path("", cart_view, name='cart_view'),
    path("add/<int:product_id>", add_to_cart, name='add_to_cart'),
    path("update/<int:item_id>", update_cart, name='update_cart'),
    path("delete/<int:item_id>", delete_from_cart, name="remove_from_cart")
]


