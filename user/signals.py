from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
import logging

from cart.models import Cart

user_logger = logging.getLogger("user")


def assign_cart_to_user(request, user):
    cart_id = request.COOKIES.get('cart_id')
    if cart_id:
        cart = Cart.objects.filter(id=cart_id).first()
        if cart and cart.user is None:
            cart.user = user
            cart.save()


def remove_cart_user(request):
    cart_id = request.COOKIES.get('cart_id')
    if cart_id:
        cart = Cart.objects.filter(id=cart_id).first()
        if cart and cart.user is not None:
            cart.user = None
            cart.save()


@receiver(user_logged_in)
def on_user_logged_in(sender, request, user, **kwargs):
    assign_cart_to_user(request, user)
    user_logger.info(f"User {user.username} logged in")


@receiver(user_logged_out)
def on_user_logged_out(sender, request, user, **kwargs):
    remove_cart_user(request)
    user_logger.info(f"User {user.username} logged out")
