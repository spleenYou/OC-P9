from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms


@login_required
def home(request):
    return render(request, 'blog/home.html')


@login_required
def add_ticket(request):
    make_review = False
    form = forms.AddTicketForm(label_suffix='')
    if 'make_review' in request.method:
        make_review = True
    if request.method == 'POST':
        form = forms.AddTicketForm(request.POST, label_suffix='')
        if form.is_valid():
            pass
    return render(request, 'blog/add_ticket.html', {'form': form, 'make_review': make_review})
