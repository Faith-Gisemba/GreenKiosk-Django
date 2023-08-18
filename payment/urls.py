from django.urls import path
from .views import create_payment, payment_list

urlpatterns = [
    path('payments/create/', create_payment, name='create_payment'),
    path('payments/', payment_list, name='payment_list'),
]
