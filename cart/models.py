from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def add_product(self, product, qty):
        if self.lines.filter(product=product):
            product_line = self.lines.get(product=product)
            product_line.quantity += int(qty)
	    product_line.total_price = int(qty)*int(product.price)
            product_line.save()
   
        else:
            product_line = self.lines.create(product=product, quantity=qty, total_price=int(product.price)*int(qty))
	product_line
        return product_line

    def cart_total(self):
        total = 0
        for i in self.lines.all():
            total += (i.product.price * i.quantity)
        return total

    def multiply(self, value, *args):
        return value * args

class CartLine(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='lines', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='lines')
    quantity = models.PositiveSmallIntegerField(default=1)
    total_price = models.BigIntegerField(default=0)
