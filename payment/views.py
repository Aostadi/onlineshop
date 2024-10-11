<<<<<<< HEAD
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def peyment(request):
    response = HttpResponseRedirect('/order/list')
    response.delete_cookie('cart_id')
    return response
=======
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def peyment(request):
    response = HttpResponseRedirect('/order/list')
    response.delete_cookie('cart_id')
    return response
>>>>>>> 35b2c6c (upload project file)
