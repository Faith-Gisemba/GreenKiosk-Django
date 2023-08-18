from django.contrib import admin

# Register your models here.
from.models import Delivery

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer_name', 'delivery_status', 'delivery_cost')
    list_filter = ('delivery_status',)
    search_fields = ('order_id', 'customer_name')

admin.site.register(Delivery, DeliveryAdmin)
