<<<<<<< HEAD

from django.contrib.auth.models import User
from django.db import models
=======
from django.db import models
from django.contrib.auth.models import User
>>>>>>> 35b2c6c (upload project file)

from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts', null=True, blank=True)
<<<<<<< HEAD
    created_at = models.DateTimeField(auto_now=True)

    def add_product(self, product, qty):
        if self.lines.filter(product=product):
            product_line = self.lines.get(product=product)
            product_line.quantity += int(qty)
            product_line.total_price = int(qty)*int(product.price)
            product_line.save()
   
        else:
            product_line = self.lines.create(product=product, quantity=qty, total_price=int(qty)*int(product.price))
        return product_line

    def cart_total(self):
        total = 0
        for i in self.lines.all():
            total += (i.product.price * i.quantity)
        return total

    def multiply(self, value, *args):
        return value * args
=======
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


>>>>>>> 35b2c6c (upload project file)

class CartLine(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='lines', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='lines')
    quantity = models.PositiveSmallIntegerField(default=1)
<<<<<<< HEAD
    total_price = models.BigIntegerField(default=0)
=======

    @property
    def total_price(self):
        return self.product.price * self.quantity
>>>>>>> 35b2c6c (upload project file)
