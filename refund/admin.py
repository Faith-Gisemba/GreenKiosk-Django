from django.contrib import admin
from .models import Refund

class RefundAdmin(admin.ModelAdmin):
    list_display = ('id', 'reason', 'refund_amount', 'processed_date')
    list_filter = ('processed_date',)
    # search_fields = ('id')
    readonly_fields = ('processed_date',)

admin.site.register(Refund, RefundAdmin)

