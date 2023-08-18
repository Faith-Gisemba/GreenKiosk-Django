from django.contrib import admin

# Register your models here.
from.models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'customer_id', 'payment_method', 'payment_status', 'payment_date', 'payment_amount')
    list_filter = ('payment_status',)
    search_fields = ('payment_id', 'customer_id')
    readonly_fields = ('payment_id',)

admin.site.register(Payment, PaymentAdmin)
