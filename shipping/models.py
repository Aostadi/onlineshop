from django.contrib.auth.models import User
from django.db import models


class Address(models.Model):
    title = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=64)
    province = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    postal_code = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} > {self.title}'
