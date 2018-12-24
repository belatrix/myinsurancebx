from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Role, User


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', )


class UserCustomAdmin(UserAdmin):
    list_display = ('username', 'is_staff', 'is_superuser', 'role')
    search_fields = ['username']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name',
                                      'last_name',
                                      'role')}),
        ('Permissions', {'fields': ('is_superuser',
                                    'is_staff',
                                    'groups',
                                    'user_permissions')}),
        ('History', {'fields': ('date_joined', 'last_login')})
    )


admin.site.register(Role)
admin.site.register(User, UserCustomAdmin)
