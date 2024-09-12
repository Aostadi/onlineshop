from django.urls import path

from .views import *

urlpatterns = [
    path('list', show_orders, name="show_orders"),
    path('submit', submit_order, name='submit_order')
]