from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product


@login_required
def cart_view(req):
    cart, _ = Cart.objects.get_or_create(user=req.user)
    return render(req, "cart/cart.html", {"cart": cart})


@login_required
def add_to_cart(req, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=req.user)

    item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart_view')


@login_required
def delete_from_cart(req, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=req.user)
    item.delete()
    return redirect('cart_view')


@login_required
def update_cart(req, item_id):
    item = get_object_or_404(CartItem, id = item_id, cart__user = req.user)
    quantity = int(req.POST.get('quantity', 1))
    item.quantity = max(1, quantity)
    item.save()
    return redirect('cart_view')
