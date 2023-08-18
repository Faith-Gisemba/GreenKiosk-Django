from django.contrib import admin
from .models import Ticket
# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ("email", "phone_number", "customer_name", "date_created", "date_updated")
admin.site.register(Ticket, TicketAdmin)