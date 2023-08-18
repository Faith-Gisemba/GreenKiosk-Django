from django.shortcuts import render, redirect
from .forms import VendorForm
from .models import Vendor

def create_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
    else:
        form = VendorForm()
    return render(request, 'vendor/create_vendor.html', {'form': form})

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor/vendor_list.html', {'vendors': vendors})
