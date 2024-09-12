from django.urls import path

from .views import show_cart, add_to_cart

urlpatterns= [
    path('show', show_cart, name='cart'),
    path('add', add_to_cart, name='add_to_cart')
]
