from django.urls import path

from .views import *

urlpatterns = [
    path('show', ShowCartView.as_view(), name='cart'),
    path('add', add_to_cart, name='add_to_cart')
]
