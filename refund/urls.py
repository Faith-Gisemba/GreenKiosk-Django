from django.urls import path
from .views import create_refund, refund_list

urlpatterns = [
    path('refunds/create/', create_refund, name='create_refund'),
    path('refunds/', refund_list, name='refund_list'),
]
