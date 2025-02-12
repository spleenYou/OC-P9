from django.shortcuts import render


def home(request):
    return render(request, 'book/home.html')
