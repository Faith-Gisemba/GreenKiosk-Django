# views.py
from django.shortcuts import render, redirect
from .models import Cart
from .forms import CartAddForm

def cart_view(request):
    if request.method == 'POST':
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.save()
            return redirect('cart')
    else:
        form = CartAddForm()

    cart_items = Cart.objects.all()  
    context = {
        'cart_items': cart_items,
        'form': form,
    }
    return render(request, 'cart/cart.html', context)













