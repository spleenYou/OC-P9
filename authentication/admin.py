from django.contrib import admin
from .models import User


@admin.register(User)
class User(admin.ModelAdmin):
    "Change the way users are displayed on the admin page"

    list_display = (
        'is_active',
        'username',
        'email',
    )
    list_filter = (
        'is_active',
    )
    search_fields = ('username', 'email')
