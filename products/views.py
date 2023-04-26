from django.views.generic import ListView, DetailView
from .models import Products
from .forms import ProductsCommentsForm


class ProductsListView(ListView):
    model = Products
    template_name = 'products/products_list.html'
    context_object_name = 'products'


class ProductsDetailView(DetailView):
    model = Products
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = ProductsCommentsForm
        return context
