from django.urls import path
from .views import create_customer, edit_customer, customer_list, customer_detail

urlpatterns = [
    path('customers/create/', create_customer, name='create_customer'),
    path('customers/<int:customer_id>/edit/', edit_customer, name='edit_customer'),
    path('customers/', customer_list, name='customer_list'),
    path('customers/<int:customer_id>/', customer_detail, name='customer_detail'),
]

