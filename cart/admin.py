from django.contrib import admin

# Register your models here.
from .models import Cart
class Cart_admin(admin.ModelAdmin):
    list_display = ("date","price","image","quantity","product_name")
admin.site.register(Cart,Cart_admin)