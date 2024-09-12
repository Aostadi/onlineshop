
from django.shortcuts import render, get_object_or_404

from .models import *
def home(request):
    product = Product.objects.all()
    return render(request, 'home/index.html', {'products':product})

def product_list(request):
    categories = Category.objects.all()
    return render(request, 'product/category.html', {'categories':categories})

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    comments = Comment.objects.filter(product__id=pk)
    return render(request, 'product/product_detail.html', {'product':product, 'comments':comments})

def category_detail(request, pk):
    category = get_object_or_404(Category, id=pk)
    products= category.products.all()
    return render(request, 'product/category_detail.html', {'products':products, 'category':category})