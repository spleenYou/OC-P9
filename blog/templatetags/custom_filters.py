from django import template
# from django.db import Q
from django.apps import apps
from blog import models

register = template.Library()


@register.filter
def is_instance(value, model_path):
    app_name, model_name = model_path.split('.')
    model = apps.get_model(app_name, model_name)
    return isinstance(value, model)


@register.filter
def can_review(user, ticket):
    if is_instance(ticket, "blog.Ticket"):
        review = models.Review.objects.filter(user=user, ticket=ticket)
        if review:
            return False
    return True
