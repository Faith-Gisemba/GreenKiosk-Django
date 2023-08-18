from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['customer_id', 'payment_method', 'payment_status', 'payment_date', 'payment_amount', 'currency_used']
