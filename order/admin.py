from django.contrib import admin

# Register your models here.
from.models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user_id', 'product_id', 'quantity', 'total_price', 'order_date', 'order_status')
    list_filter = ('order_status',)
    search_fields = ('order_id', 'user_id', 'product_id')
    readonly_fields = ('order_date',)

    fieldsets = (
        ('Order Information', {
            'fields': ('order_id', 'user_id', 'product_id', 'quantity')
        }),
        ('Payment Details', {
            'fields': ('total_price',)
        }),
        ('Additional Information', {
            'fields': ('items', 'order_status', 'order_date')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(self.readonly_fields)
        if obj:  # Editing an existing object
            readonly_fields.append('order_id')
        return readonly_fields
    
admin.site.register(Order,OrderAdmin)    