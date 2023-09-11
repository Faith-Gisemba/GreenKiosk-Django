from django import forms
from .models import Cart

class CartAddForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['product_name', 'quantity', 'image', 'price', 'date']
