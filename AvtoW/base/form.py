from django import forms
from .models import *


class homeList(forms.Form):
    article = forms.SlugField()
    name = forms.CharField(max_length=150)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.all())
    foto = forms.ImageField()
