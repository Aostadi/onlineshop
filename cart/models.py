from django.db import models
from django.contrib.auth.models import User

from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_ordered = models.BooleanField(default=False)

    def add_product(self, product, qty):
        product_line, created = self.lines.get_or_create(product=product)
        if not created:
            product_line.quantity += int(qty)
            product_line.save()
        return product_line

    @property
    def total_price(self):
        return sum(line.product.price * line.quantity for line in self.lines.all())

    @property
    def items(self):
        return self.lines.all()

    class Meta:
        get_latest_by = 'updated_at'

    def __str__(self):
        return f"{self.user} > {self.created_at}"



class CartLine(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='lines', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='lines')
    quantity = models.PositiveSmallIntegerField(default=1)

    @property
    def total_price(self):
        return self.product.price * self.quantity
