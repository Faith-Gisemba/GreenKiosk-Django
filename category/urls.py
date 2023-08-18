from django.urls import path
from .views import create_category, edit_category, category_list, category_detail

urlpatterns = [
    path('categories/create/', create_category, name='create_category'),
    path('categories/<int:category_id>/edit/', edit_category, name='edit_category'),
    path('categories/', category_list, name='category_list'),
    path('categories/<int:category_id>/', category_detail, name='category_detail'),
]
