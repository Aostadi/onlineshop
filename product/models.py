from django.contrib.auth.models import User
from django.db import models


class Attribute(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name

class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='values')
    value = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.attribute.name} > {self.value}'

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name="products")
    attribute = models.ManyToManyField(AttributeValue, related_name='products')
    price = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    RATING_CHOICE = (
        (1, 'worse'),
        (2, 'bad'),
        (3, 'not bad'),
        (4, 'good'),
        (5, 'great')
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='Anonymous')
    comment = models.TextField(max_length=512)
    rating = models.CharField(max_length=1, choices=RATING_CHOICE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product.name} > {self.user.username}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return f'{self.product.name}'