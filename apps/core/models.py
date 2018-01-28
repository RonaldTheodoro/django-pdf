from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(default=0.00, max_digits=18, decimal_places=2)

    class Meta:
        db_table = 'tutorial_product'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=None)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(default=0.00, max_digits=18, decimal_places=2)
    customer = models.ForeignKey(User, on_delete=None)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tutorial_product_sale'
        verbose_name = 'sale'
        verbose_name_plural = 'sale'

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        super(Sale, self).save(*args, **kwargs)

    def __str__(self):
        return self.product.title