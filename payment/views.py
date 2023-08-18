from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment

def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'payment/create_payment.html', {'form': form})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment/payment_list.html', {'payments': payments})

