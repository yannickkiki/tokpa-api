from rest_framework import serializers

from product.models import Product
from order.models import Order


class OrderSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        assert validated_data.get('cart')  # confirm that there is a cart in the fields and that the cart is not empty

        products_ordered_ids = validated_data['cart'].keys()
        products_ordered = list(Product.objects.filter(id__in=products_ordered_ids))
        assert len(products_ordered) == len(products_ordered_ids)  # confirm that all products ordered exists in the db

        amount = 0
        for product in products_ordered:
            quantity_ordered = validated_data['cart'][str(product.id)]
            amount += product.price_per_unit * quantity_ordered

        validated_data['amount'] = amount
        return super().create(validated_data)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('amount', )
