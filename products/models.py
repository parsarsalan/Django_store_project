from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class CustomCommentManager(models.Manager):
    def get_queryset(self):
        return super(CustomCommentManager, self).get_queryset().filter(active=True)


class ProductsComments(models.Model):
    STARS_CHOICES = (
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'normal'),
        ('4', 'good'),
        ('5', 'perfect')
    )
    text = models.TextField(verbose_name="comment text")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='comments')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    stars = models.CharField(max_length=10, choices=STARS_CHOICES, blank=True, verbose_name="Score of Product")
    active = models.BooleanField(default=True)


# -> Manager
    objects = models.Manager()
    active_comments = CustomCommentManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])

    def __str__(self):
        return f'{self.author}'
