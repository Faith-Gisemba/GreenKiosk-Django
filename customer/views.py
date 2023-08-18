from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerForm
from .models import Customer

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer/create_customer.html', {'form': form})

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, customer_id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/edit_customer.html', {'form': form, 'customer': customer})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customers': customers})

def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, customer_id=customer_id)
    return render(request, 'customer/customer_detail.html', {'customer': customer})
