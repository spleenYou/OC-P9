from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms


@login_required
def home(request):
    return render(request, 'blog/home.html')


@login_required
def add_ticket(request):
    form = forms.AddTicketForm(label_suffix='')
    if request.method == 'POST':
        form = forms.AddTicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'blog/add_ticket.html', {'form': form, 'action': 'Créer'})


@login_required
def del_ticket(request):
    pass


@login_required
def update_ticket(request):
    pass
