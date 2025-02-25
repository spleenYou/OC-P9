from django import forms
from django.db.models.fields.files import ImageFieldFile
from . import models


class CustomImageFieldWidget(forms.ClearableFileInput):
    template_name = 'ImageField.html'

    def get_context(self, name, value, attrs, **kwargs):
        context = super().get_context(name, value, attrs)
        context['widget']['is_image'] = isinstance(value, ImageFieldFile)
        return context


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
            'image': CustomImageFieldWidget()
        }


class CustomRatingFieldWidget(forms.NumberInput):
    template_name = 'PositiveSmallField.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        return context


class AddReviewForm(forms.ModelForm):

    class Meta:
        model = models.Review
        fields = [
            'headline',
            'rating',
            'body',
        ]
        labels = {
            'rating': 'Notation',
            'headline': 'Titre',
            'body': 'Critique',
        }
        widgets = {
            'rating': CustomRatingFieldWidget()
        }
