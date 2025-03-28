from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.models import Cart


@login_required
def create_order(req):
    cart = req.user.cart

    if cart.items.exists():
        order = Order.objects.create(user=req.user)
        for item in cart.items.all():
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        cart.items.all().delete()
        return redirect('order_success', order_id=order.id)
    return redirect('cart_view')


@login_required
def order_success(req, order_id):
    order = Order.objects.get(id=order_id)
    return render(req, 'orders/order_success.html', {"order": order})


@login_required
def order_list(req):
    orders = req.user.orders.all()
    return render(req, "orders/order_list.html", {"orders": orders})
