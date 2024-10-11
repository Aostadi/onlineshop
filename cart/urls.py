from django.urls import path

<<<<<<< HEAD
from .views import show_cart, add_to_cart

urlpatterns= [
    path('show', show_cart, name='cart'),
=======
from .views import *

urlpatterns = [
    path('show', ShowCartView.as_view(), name='cart'),
>>>>>>> 35b2c6c (upload project file)
    path('add', add_to_cart, name='add_to_cart')
]
