from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from cart.models import Cart
from order.models import *
from shipping.models import Address

from .models import Post


def show_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'product/show_orders.html', {'orders': orders})


@login_required
def submit_order(request):
    cart_id = request.COOKIES.get('cart_id')
    user = request.user
    if request.method == 'POST':
        cart = Cart.objects.get(id=cart_id)
        cart_items = cart.lines.all()
        address_id = request.POST.get("address")
        post = Post.objects.get(id=request.POST.get("post_id"))
        cart_total = int(cart.cart_total()) + int(post.cost)

        Order.objects.create(
            user=user,
            products=cart,
            address=Address.objects.get(id=address_id),
            post=post
        )
        return render(request,
                      'product/submit_order.html',
                      {
                          'posts': post,
                          'cart_items':cart_items,
                          'cart_total':cart_total
                      })
    return Http404
