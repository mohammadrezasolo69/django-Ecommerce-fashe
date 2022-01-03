from .cart import Cart
from ecommerce_product.forms import AddCart
from ecommerce_product.models import StoreProducts
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


@login_required
def detail_cart(request):
    cart = Cart(request)
    return render(request, 'cart/detail_cart.html', context={'cart': cart})


@require_POST
def add_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(StoreProducts, id=product_id, is_active=True)
    form = AddCart(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['count'])
    return redirect('cart:detail_cart')


def remove_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(StoreProducts, id=product_id, is_active=True)
    cart.remove(product=product)
    return redirect('cart:detail_cart')