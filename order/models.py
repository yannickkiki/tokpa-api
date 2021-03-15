from django.db import models
from django.contrib.postgres.fields import JSONField

from user.models import User

from xlib.enums import PaymentMethod


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = JSONField(default=dict)  # [{product_id: quantity}, ...]
    amount = models.IntegerField()

    delivery_address_district = models.CharField(max_length=255)
    delivery_address_indication = models.CharField(max_length=255)

    payment_method = models.CharField(max_length=255, choices=PaymentMethod.values())
    payment_status = 'paid'

    class Meta:
        db_table = '"tokpa"."order"'
