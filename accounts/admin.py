# users/admin.py

# from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from django.contrib.auth.forms import UserChangeForm

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ', '.join(groups)
    group.short_description = 'Grupos'

    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'group']
    list_filter = ['username', 'groups']

    fieldsets = (
        (
            'Información básica', {
                'classes': ('wide',),
                'fields': ('username', 'password'),
            }
        ),
        (
            'Información personal', {
                'classes': ('wide',),
                'fields': ('first_name', 'last_name', 'email'),
            }
        ),
        (
            'Permisos', {
                'classes': ('collapse',),
                'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            }
        ),
        (
            'Fechas Importantes', {
                'classes': ('collapse',),
                'fields': ('last_login', 'date_joined'),
            }
        ),
    )
    # fieldsets = UserAdmin.fieldsets

    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('email', 'first_name', 'last_name')
            }
        ),
    ) + UserAdmin.add_fieldsets


admin.site.register(CustomUser, CustomUserAdmin)
