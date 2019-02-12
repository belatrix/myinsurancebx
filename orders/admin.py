from django.contrib import admin
from .models import Order, Attachment, OrderStatus, AutoRepairShop


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'hash', 'uploaded_by', 'created_at', 'modified_at')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_by', 'status', 'budget', 'created_at', 'priority')


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_default', 'ordering')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(AutoRepairShop)
