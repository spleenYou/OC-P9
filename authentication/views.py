from django.shortcuts import render

from . import forms


def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'authentication/login.html', {'form': form})


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = form.SignupForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'authentication/signup.html', {'form': form})
