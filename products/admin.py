from django.contrib import admin
from .models import Products, ProductsComments


class CommentInLine(admin.TabularInline):
    model = ProductsComments
    fields = ('product', 'author', 'stars', 'active',)
    extra = 1   # -> show only 1 extra comment field


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    fields = ('title', 'user', 'active', 'price', 'description',)
    inlines = [
        CommentInLine        # -> show comment in line in admin page
    ]


@admin.register(ProductsComments)
class ProductsCommentsAdmin(admin.ModelAdmin):
    fields = ('text', 'product', 'author', 'stars', 'active',)

