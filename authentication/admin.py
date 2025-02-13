from django.contrib import admin
from .models import User


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
