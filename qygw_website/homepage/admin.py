from django.contrib import admin
from .models import Kehu

@admin.register(Kehu)
class KehuAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'company', 'inquiry_type', 'created_at')
    list_filter = ('inquiry_type', 'created_at')
    search_fields = ('name', 'phone', 'email', 'company', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 20
