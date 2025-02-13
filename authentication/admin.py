from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import User

# admin.site.register(User, UserAdmin)


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = (
        'is_active',
        'username',
        'email',
        'role',
    )
    list_filter = (
        'role',
        'is_active',
    )
    search_fields = ('username', 'email')
