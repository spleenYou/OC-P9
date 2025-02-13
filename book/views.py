from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'book/home.html')


@login_required
def test(request):
    return render(request, 'book/test.html')
