from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['username', 'email', 'is_superuser']
    fieldsets = (
        (
            None,
            {'fields': ('username', 'password')}
        ),
        (
            _('Personal Info'),
            {'fields': ('first_name',
                        'last_name',
                        'email',
                        'thumbnail',
                        'age',
                        'phone',
                        'country',

                        )
             }
        ),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (
            _('Important dates'),
            {'fields': ('last_login', 'date_joined')}
        ),
    )
    add_fieldsets = (
        (
            None,
            {'classes': ('wide',),
             'fields': (
                 'username',
                 'email',
                 'password1',
                 'password2',
                        ),
             }
        ),
    )


admin.site.register(models.User, UserAdmin)