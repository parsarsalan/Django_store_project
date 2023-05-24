from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.utils.translation import gettext as _

from products.models import Products
from .cart import Cart
from .forms import AddToCartProductForm


def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['update_add_cart'] = AddToCartProductForm(initial={
            'quantity': item['quantity'],
            'inplace': True,

        })
    return render(request, 'cart/cart_detail.html', {'cart': cart, })


@require_POST
def add_to_cart_view(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Products, id=pk)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add_to_cart(product, quantity, replace_current_quantity=cleaned_data['inplace'])

    return redirect('cart:cart_detail')


@require_POST
def remove_product_in_cart(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Products, id=pk)

    cart.remove_from_cart(product)
    return redirect('cart:cart_detail')


@require_POST
def clear_cart(request):
    cart = Cart(request)
    if len(cart):
        cart.clear_all()
        messages.success(request, _('your products in cart cleared successfully'))
    else:
        messages.warning(request, _('your cart already empty'))

    return redirect('cart:cart_detail')
