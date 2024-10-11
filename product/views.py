<<<<<<< HEAD

from django.shortcuts import render, get_object_or_404

from .models import *
=======
from django.shortcuts import render, get_object_or_404

from .models import *


>>>>>>> 35b2c6c (upload project file)
def home(request):
    product = Product.objects.all()
    return render(request, 'home/index.html', {'products':product})

<<<<<<< HEAD
=======

>>>>>>> 35b2c6c (upload project file)
def product_list(request):
    categories = Category.objects.all()
    return render(request, 'product/category.html', {'categories':categories})

<<<<<<< HEAD
def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    comments = Comment.objects.filter(product__id=pk)
    return render(request, 'product/product_detail.html', {'product':product, 'comments':comments})
=======

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    # comments = Comment.objects.filter(product__id=pk)
    return render(request, 'product/product_detail.html', {'product':product})

>>>>>>> 35b2c6c (upload project file)

def category_detail(request, pk):
    category = get_object_or_404(Category, id=pk)
    products= category.products.all()
    return render(request, 'product/category_detail.html', {'products':products, 'category':category})