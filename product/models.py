from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.id})"

    class Meta:
        verbose_name_plural = "Product Categories"
        db_table = '"tokpa"."product_category"'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price_per_unit = models.IntegerField()
    unit_name = models.CharField(max_length=100)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.price_per_unit} FCFA/{self.unit_name})"

    class Meta:
        db_table = '"tokpa"."product"'
