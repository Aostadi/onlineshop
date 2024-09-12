from django.urls import path
from .views import *
urlpatterns = [
    path('address/add', add_address, name='add_address')
]