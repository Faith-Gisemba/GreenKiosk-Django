from django.shortcuts import render, get_object_or_404, redirect
from .forms import CartForm
from .models import Cart

def edit_cart(request, cart_id):
    cart = get_object_or_404(Cart, pk=cart_id)
    if request.method == 'POST':
        form = CartForm(request.POST, request.FILES, instance=cart)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
    else:
        form = CartForm(instance=cart)
        return render(request, 'edit_cart.html', {'form': form, 'cart': cart})


def create_cart(request):
    if request.method == 'POST':
        form = CartForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
        return redirect('cart_list')
    else:
        form = CartForm()
        return render(request, 'cart/create_cart.html', {'form': form})


def cart_list(request):
    carts = Cart.objects.all()
    return render(request, 'cart/cart_list.html', {'carts': carts})

def cart_detail(request, cart_id):
    cart = get_object_or_404(Cart, pk=cart_id)
    return render(request, 'cart_detail.html', {'cart': cart})







