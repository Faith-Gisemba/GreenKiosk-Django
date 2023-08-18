from django.urls import path
from .views import create_vendor, vendor_list

urlpatterns = [
    path('vendors/create/', create_vendor, name='create_vendor'),
    path('vendors/', vendor_list, name='vendor_list'),
]
