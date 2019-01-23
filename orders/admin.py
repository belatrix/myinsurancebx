from django.contrib import admin
from .models import Order, Attachment, OrderStatus


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'hash', 'uploaded_by', 'created_at', 'modified_at')


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_default')


admin.site.register(Order)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(Attachment, AttachmentAdmin)
