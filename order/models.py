from django.contrib.auth.models import User
from django.db import models

from cart.models import Cart
from shipping.models import Address


class Post(models.Model):
    name = models.CharField(max_length=32, unique=True)
    cost = models.BigIntegerField()

    def __str__(self):
        return f"{self.name} > {self.cost}"


class Order(models.Model):
    STATUS_CHOICES = (
        (1, 'not payed'),
        (2, 'pending'),
        (3, 'sent')
    )
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    products = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    status = models.IntegerField( choices=STATUS_CHOICES)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.user.username} > {self.address.title}'