from django import forms
from . import models

from django.forms.widgets import ClearableFileInput


class ImageFieldWidgetWithPreview(ClearableFileInput):
    template_name = 'ImageField.html'


class AddTicketForm(forms.ModelForm):

    class Meta:
        model = models.Ticket
        fields = [
            'title',
            'description',
            'image',
        ]
        labels = {
            'title': "Titre"
        }
        widgets = {
            'image': ImageFieldWidgetWithPreview()
        }
