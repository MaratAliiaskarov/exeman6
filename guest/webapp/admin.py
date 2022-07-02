from django.contrib import admin

# Register your models here.
from webapp.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'guest_name', 'from_email', 'status']
    list_display_links = ['guest_name']
    list_filter = ['guest_name']
    search_fields = ['guest_name', 'content', 'status']
    fields = ['guest_name', 'from_email', 'content', 'created_at', 'updated_at']
    readonly_fields = ['status', 'created_at', 'updated_at']


admin.site.register(Book, BookAdmin)
