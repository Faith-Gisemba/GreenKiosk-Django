from django.contrib import admin

# Register your models here.
from.models import Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'stock', 'date_created', 'date_updated')
    list_filter = ('status',)
    search_fields = ('name', 'description')
    readonly_fields = ('date_created', 'date_updated')

    fieldsets = (
        ('Category Information', {
            'fields': ('name', 'description', 'status', 'image')
        }),
        ('Stock Details', {
            'fields': ('stock',)
        }),
        ('Date Information', {
            'fields': ('date_created', 'date_updated'),
            'classes': ('collapse',),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(self.readonly_fields)
        if obj:  # Editing an existing object
            readonly_fields.extend(['date_created', 'date_updated'])
        return readonly_fields

admin.site.register(Category,CategoryAdmin)    