from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserCustomAdmin(UserAdmin):
    list_display = ('username', 'is_superuser', 'is_inspector', 'is_from_insurance', 'is_from_auto_repair_shop')
    search_fields = ['username']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name',
                                      'last_name')}),
        ('Permissions', {'fields': ('is_superuser',
                                    'is_staff',
                                    'is_inspector',
                                    'is_from_insurance',
                                    'is_from_auto_repair_shop',
                                    'groups',
                                    'user_permissions')}),
        ('History', {'fields': ('date_joined', 'last_login')})
    )


admin.site.register(User, UserCustomAdmin)
