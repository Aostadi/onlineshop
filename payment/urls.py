from django.urls import path
from .views import *
urlpatterns = [
    path('pay', peyment, name='payment')
]