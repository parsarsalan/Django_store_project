from django.urls import path

from .views import cart_detail_view, add_to_cart_view, remove_product_in_cart, clear_cart

app_name = 'cart'

urlpatterns = [
    path('', cart_detail_view, name='cart_detail'),
    path('add/<int:pk>/', add_to_cart_view, name='cart_add_product'),
    path('remove/<int:pk>/', remove_product_in_cart, name='cart_remove_product'),
    path('clear/<int:pk>/', clear_cart, name='cart_clear')
]
