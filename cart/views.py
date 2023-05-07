from django.shortcuts import render, get_object_or_404, redirect

from products.models import Products
from .cart import Cart
from .forms import CartProductForm


def cart_detail_view(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def add_to_cart_view(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Products, pk)
    form = CartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add_to_cart(product, quantity)

    return redirect('cart_detail')
