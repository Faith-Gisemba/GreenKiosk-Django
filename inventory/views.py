from django.shortcuts import render,redirect
from .forms import productUploadForm
from .models import Product



# Create your views here.

def product_upload_view(request):
    if request.method == 'POST':
        form = productUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = productUploadForm()

    return render(request, "inventory/product_upload.html", {"form": form})

def products_list(request):
    products = Product.objects.all()
    return render(request, "inventory/products_list.html", {"products": products})

def products_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, "inventory/product_detail.html", {"product": product})

def products_update_view(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = productUploadForm(request.POST, instance = product)
        if form.is_valid():
            form.save()
        return redirect("product_detail_view", id=id)
    else:
        form = productUploadForm(instance = product)
        return render(request, "inventory/edit_product.html",{"form":form})
    
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("product_list_view")


    
    
    
    
    

    
    


