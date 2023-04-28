from django.contrib import admin
from .models import Products, ProductsComments


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    fields = ('title', 'user', 'active', 'price', 'description',)


@admin.register(ProductsComments)
class ProductsCommentsAdmin(admin.ModelAdmin):
    fields = ('text', 'product', 'author', 'stars', 'active',)

