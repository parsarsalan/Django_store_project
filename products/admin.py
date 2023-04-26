from django.contrib import admin
from.models import Products, ProductsComments


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    fields = ('title', 'user', 'datetime_created', 'datetime_modified', 'active',)


@admin.register(ProductsComments)
class ProductsCommentsAdmin(admin.ModelAdmin):
    fields = ('product_id', 'product_user', 'stars', 'active', 'datetime_created',)

