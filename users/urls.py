from django.urls import path
from .views import logout_view, login_view, register_view, profile_view, edit_profile, change_password, order_history


urlpatterns = [
    path("logout/", logout_view, name='logout'),
    path("login/", login_view, name='login'),
    path("register/", register_view, name='register'),
    path("profile/", profile_view, name="profile"),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/change-password/', change_password, name='change_password'),
    path('profile/orders/', order_history, name='order_history')
]
