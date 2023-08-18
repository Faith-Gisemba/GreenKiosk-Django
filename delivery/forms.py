from django import forms
from .models import Delivery

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['customer_name', 'delivery_address', 'delivery_status', 'delivery_date', 'delivery_method', 'order_id', 'delivery_cost']
