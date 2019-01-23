from django.contrib import admin
from .models import Order, Attachment


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'hash', 'uploaded_by', 'created_at', 'modified_at')


admin.site.register(Order)
admin.site.register(Attachment, AttachmentAdmin)
