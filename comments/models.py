from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Comment(models.Model):
    RATING_CHOICE = (
        (1, 'Worse'),
        (2, 'Bad'),
        (3, 'Not Bad'),
        (4, 'Good'),
        (5, 'Great')
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='Anonymous')
    comment = models.TextField(max_length=512)
    rating = models.IntegerField( choices=RATING_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} > {self.product.name} > {self.get_rating_display()}'
