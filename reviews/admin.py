from django.contrib import admin
from .models import Review
# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('comment', 'rating', 'date_created', 'date_updated')
    list_filter = ('rating', 'date_created')
    search_fields = ('comment',)
admin.site.register(Review,ReviewAdmin)