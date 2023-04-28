from django.urls import path

from .views import ProductsDetailView, ProductsListView, ProductsCommentView

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('<int:pk>', ProductsDetailView.as_view(), name='product_detail'),
    path('<int:pk>/comments/', ProductsCommentView.as_view(), name='product_comment'),

]
