from django.urls import path
from .views import *
urlpatterns = [
    path('list/', product_list, name='product_list'),
    path('detail/<int:pk>', product_detail, name='product_detail'),
    path('category/<int:pk>', category_detail, name='category_detail')
]