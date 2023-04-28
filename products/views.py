from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView


from .models import Products, ProductsComments
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
        context['comment_form'] = ProductsCommentsForm()
        return context


class ProductsCommentView(CreateView):
    model = ProductsComments
    form_class = ProductsCommentsForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        pk = int(self.kwargs['pk'])
        obj.product = get_object_or_404(Products, id=pk)
        return super().form_valid(form)

