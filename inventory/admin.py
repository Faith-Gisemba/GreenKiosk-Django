from django.contrib import admin


# Register your models here.
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display=("name","stock","price","date_created","date_updated","description")

admin.site.register(Product,ProductAdmin)