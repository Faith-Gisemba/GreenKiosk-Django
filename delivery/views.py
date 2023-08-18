from django.shortcuts import render, redirect, get_object_or_404
from .forms import DeliveryForm
from .models import Delivery

def create_delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('delivery_list')
    else:
        form = DeliveryForm()
    return render(request, 'delivery/create_delivery.html', {'form': form})

def edit_delivery(request, delivery_id):
    delivery = get_object_or_404(Delivery, pk=delivery_id)
    if request.method == 'POST':
        form = DeliveryForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
            return redirect('delivery_list')
    else:
        form = DeliveryForm(instance=delivery)
    return render(request, 'delivery/edit_delivery.html', {'form': form, 'delivery': delivery})

def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, 'delivery/delivery_list.html', {'deliveries': deliveries})

def delivery_detail(request, delivery_id):
    delivery = get_object_or_404(Delivery, pk=delivery_id)
    return render(request, 'delivery/delivery_detail.html', {'delivery': delivery})
