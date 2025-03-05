from django import forms
from . import models


class CustomImageFieldWidget(forms.ClearableFileInput):
    "template name for change the way it will be display"
    template_name = 'ImageField.html'


class AddTicketForm(forms.ModelForm):

    def get_title(self):
        return self.title

    class Meta():
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
    "template name for change the way it will be display"

    template_name = 'PositiveSmallField.html'


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
