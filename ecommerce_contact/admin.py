from django.contrib import admin
from .models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'send', 'is_read')
    list_editable = ('is_read',)
    list_filter = ('is_read', 'send')
