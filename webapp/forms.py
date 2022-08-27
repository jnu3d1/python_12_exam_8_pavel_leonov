from django import forms
from django.forms import widgets

from webapp.models import Product


class SearchForm(forms.Form):
    search = forms.CharField(label='Поиск', max_length=50, required=False)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'image']
        widgets = {
            'description': widgets.Textarea,
        }
