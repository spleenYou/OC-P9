from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'blog/home.html')


@login_required
def test(request):
    return render(request, 'blog/test.html')
