from django.urls import path
from .views import product_upload_view, products_update_view
from .views import products_list
from .views import products_detail

urlpatterns = [
    path("products/upload/" ,product_upload_view,name ="product_upload_view"),
    path("products/list",products_list, name = "products_list_view"),
    path("products/<int:id>/", products_detail, name = "product_detail_view"),
    path("products/edit/<int:id>/", products_update_view, name= "product_update"),
    # path('products/<int:id>/delete/',delete_product_view, name='delete_product')
]






