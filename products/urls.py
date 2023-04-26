from django.urls import path

from .views import ProductsDetailView, ProductsListView

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('<int:pk>', ProductsDetailView.as_view(), name='product_detail'),

]
