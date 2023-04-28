from django.forms import ModelForm
from .models import ProductsComments


class ProductsCommentsForm(ModelForm):
    class Meta:
        model = ProductsComments
        fields = ('text', 'stars',)

