import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Payment
from orders.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def create_checkout_session(req, order_id):
    order = Order.objects.get(id=order_id)
    if Payment.objects.filter(order=order).exists():
        return redirect('order_success', order_id=order.id)

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': f"Order {order.id}",
                        },
                        'unit_amount': int(order.total_price() * 100),
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=req.build_absolute_uri(f"/payments/success/{order.id}/"),
            cancel_url=req.build_absolute_uri(f"/payments/cancel/{order.id}/"),
        )

        Payment.objects.create(
            order=order,
            stripe_payment_intent=session.payment_intent,
            amount=order.total_price(),
            status="pending"
        )

        return redirect(session.url)

    except  Exception as e:
        return render(req, "payments/error.html", {"error": str(e)})


@login_required
def payment_success(req, order_id):
    order = Order.objects.get(id=order_id)
    payment = Payment.objects.get(order=order)
    payment.status = "paid"
    payment.save()
    order.status = "processing"
    order.save()
    return render(req, "payments/success.html", {"order": order})


@login_required
def payment_cancelled(req, order_id):
    order = Order.objects.get(id=order_id)
    return render(req, "payments/cancel.html", {"order": order})

