from django.urls import path
from .views import payment_success, create_checkout_session, payment_cancelled


urlpatterns = [
    path("checkout/<int:order_id>/", create_checkout_session, name="checkout"),
    path("success/<int:order_id>/", payment_success, name="payment_success"),
    path("cancel/<int:order_id>/", payment_cancelled, name="payment_cancel")
]
