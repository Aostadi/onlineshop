from datetime import datetime, timedelta

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from cart.models import Cart
from order.models import Post
from product.models import Product
from shipping.models import Address
from django.views.generic import TemplateView, View


class ShowCartView(TemplateView):
    template_name = 'product/show_cart.html'

    def get(self, request, *args, **kwargs):
        cart = self.get_cart(request)
        if cart:
            addresses = Address.objects.filter(user=request.user if request.user.is_authenticated else None)
            shipping_methods = Post.objects.all()
            return self.render_to_response(
                          {
                              'cart': cart,
                              'addresses': addresses,
                              'shipping_methods': shipping_methods
                          })
        else:
            return HttpResponse("You don't have cart")

    def get_cart(self, request):
        if request.user.is_authenticated:
            past_days = self.get_past_date(days=3)
            return Cart.objects.filter(
                user=request.user,
                updated_at__gte=past_days,
                is_ordered=False).latest()
        else:
            cart_id = request.COOKIES.get('cart_id')
            if cart_id is not None:
                return get_object_or_404(
                    Cart,
                    id=int(cart_id),
                    user=None)

    @staticmethod
    def get_past_date(days):
        return datetime.now() - timedelta(days=days)


def add_to_cart(request):
    response = HttpResponseRedirect(request.POST.get('next'))
    cart_id = request.COOKIES.get('cart_id')
    cart, created = Cart.objects.get_or_create(
        id=cart_id,
        user=request.user if request.user.is_authenticated else None)
    product_id = request.POST.get('product_id')
    product = get_object_or_404(
        Product,
        id=product_id,
        is_available=True)
    cart.add_product(product, request.POST.get('qty'))
    response.set_cookie('cart_id', cart.id)
    return response
