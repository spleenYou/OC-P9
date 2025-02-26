from django import template
from django.apps import apps

register = template.Library()


@register.filter
def is_instance(value, model_path):
    app_name, model_name = model_path.split('.')
    model = apps.get_model(app_name, model_name)
    return isinstance(value, model)
