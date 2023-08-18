from django.urls import path
from .views import create_order, edit_order, order_list, order_detail

urlpatterns = [
    path('orders/create/', create_order, name='create_order'),
    path('orders/<int:order_id>/edit/', edit_order, name='edit_order'),
    path('orders/', order_list, name='order_list'),
    path('orders/<int:order_id>/', order_detail, name='order_detail'),
]
