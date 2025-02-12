from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=63,
        label=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nom d’utilisateur'})
    )
    password = forms.CharField(
        max_length=63,
        label=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'})
    )


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = {
            'username',
            'email',
            'first_name',
            'last_name',
            'role',
        }
