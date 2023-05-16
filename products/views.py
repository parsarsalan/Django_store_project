from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from django.views.generic import ListView, DetailView, CreateView


from .models import Products, ProductsComments
from .forms import ProductsCommentsForm
from cart.forms import AddToCartProductForm


class ProductsListView(ListView):
    model = Products
    template_name = 'products/products_list.html'
    context_object_name = 'products'
    paginate_by = 2


class ProductsDetailView(DetailView):
    model = Products
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = ProductsCommentsForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        return context


class ProductsCommentView(CreateView):
    model = ProductsComments
    form_class = ProductsCommentsForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        pk = int(self.kwargs['pk'])
        obj.product = get_object_or_404(Products, id=pk)
        messages.success(self.request, _('Your comment successfully added'))
        return super().form_valid(form)

