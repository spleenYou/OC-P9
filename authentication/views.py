from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from . import forms


def login_page(request):
    if request.user.is_authenticated:
        return redirect('test')
    form = forms.LoginForm()
    tab_error = []
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('test')
            else:
                tab_error.append('Identifiants invalides')
        else:
            errors = form.errors
            for error in errors:
                tab_error.append(errors[error])
    return render(request, 'authentication/login.html', {'form': form, 'errors': tab_error})


def signup_page(request):
    form = forms.SignupForm()
    tab_error = []
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('test')
        else:
            errors = form.errors
            for error in errors:
                tab_error.append(errors[error])
    return render(request, 'authentication/signup.html', {'form': form, 'errors': tab_error})


def logout_user(request):
    logout(request)
    return redirect('login')
