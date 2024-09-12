from django.contrib.auth.models import User
from django.db import models
from product.models import Product
from shipping.models import Address
from cart.models import Cart


class Post(models.Model):
    name = models.CharField(max_length=32, unique=True)
    cost = models.BigIntegerField(default=0)


class Order(models.Model):
    STATUS_CHOICES =(
        ('1', 'pending'),
        ('2', 'sent'),
        ('3', 'received')
    )
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    products = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, default='None')

    def __str__(self):
        return f'{self.user.username} > {self.address.title}'