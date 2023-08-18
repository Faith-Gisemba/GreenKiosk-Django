from django.shortcuts import render, redirect
from .forms import RefundForm
from .models import Refund

def create_refund(request):
    if request.method == 'POST':
        form = RefundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('refund_list')
    else:
        form = RefundForm()
    return render(request, 'refund/create_refund.html', {'form': form})

def refund_list(request):
    refunds = Refund.objects.all()
    return render(request, 'refund/refund_list.html', {'refunds': refunds})

