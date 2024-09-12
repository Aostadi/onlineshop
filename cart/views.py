from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render
from cart.models import Cart
from product.models import Product
from shipping.models import Address
from order.models import Post


def show_cart(request):
    try:
        cart_id = request.COOKIES.get('cart_id')
        cart = Cart.objects.get(id=cart_id)
    except:
        return HttpResponse("You don't have cart")
    cart_items = cart.lines.all()

    cart_total = cart.cart_total()
    if request.user.is_authenticated:
        addresses = Address.objects.filter(user=request.user)
    else:
        addresses = None
    shipping_methods = Post.objects.all()
    return render(request, 'product/show_cart.html',
                  {
                      'cart_items':cart_items,
                      'cart_total':cart_total,
                      'addresses': addresses,
                      'shipping_methods': shipping_methods
                  })

def add_to_cart(request):
    response = HttpResponseRedirect(request.POST.get('next'))
    cart_id =request.COOKIES.get('cart_id')
    if cart_id is None:
        cart = Cart.objects.create()
        response.set_cookie(key='cart_id', value=cart.id)
    else:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            raise Http404
    if request.user.is_authenticated:
        if cart.user is not None and cart.user != request.user:
            raise Http404
        cart.user = request.user
        cart.save()
    product_id = request.POST.get('product_id', None)
    if product_id is not None:
        try:
            product = Product.objects.get(id=product_id)
        except:
            raise Http404
        else:
            cart.add_product(product, request.POST.get('qty'))
    return response