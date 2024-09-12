from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .forms import AddAddressForm
from .models import Address
from order.models import Post


@login_required
@require_http_methods(['GET', 'POST'])
def add_address(request):
    if request.method == 'POST':
        form = AddAddressForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('cart')
    else:
        form = AddAddressForm

    return render(request, 'product/add_address.html', {'form': form})
