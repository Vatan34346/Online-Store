from django.db import models
from django.conf import settings
from orders.models import Order


class Payment(models.Model):
    PAYMENT_STATUSES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    ]
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
    stripe_payment_intent = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUSES, default="pending")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Payment: {self.id} - {self.order} - {self.status}"

