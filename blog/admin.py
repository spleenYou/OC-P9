from django.contrib import admin
from .models import Ticket, Review, UserFollows


@admin.register(Ticket)
class Ticket(admin.ModelAdmin):
    fields = (
        'user',
        'title',
        'description',
        'image',
    )
    list_display = (
        'id',
        'title',
        'user',
        'time_created',
    )
    list_filter = (
        'user',
        'time_created',
    )
    list_display_links = (
        'id',
        'title',
    )
    search_fields = ['title']


@admin.register(Review)
class Review(admin.ModelAdmin):
    fields = (
        'ticket',
        'user',
        'headline',
        'body',
        'rating',
    )
    list_display = (
        'id',
        'headline',
        'user',
        'rating',
        'time_created',
    )
    list_filter = (
        'user',
        'rating',
        'time_created',
    )
    list_display_links = (
        'id',
        'headline',
    )
    search_fields = ('headline', 'body')


@admin.register(UserFollows)
class UserFollows(admin.ModelAdmin):
    list_display = (
        'user',
    )
    list_filter = (
        'user',
    )
    search_fields = ['followed_user']
