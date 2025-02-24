from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.db.models import Q
from . import forms, models


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    return render(request, 'blog/home.html', {'tickets': tickets})


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
    return render(request, 'blog/add_ticket.html', {'form': form})


@login_required
def del_ticket(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('my_posts')
    return render(request, 'blog/del_ticket.html', {'ticket': ticket})


@login_required
def update_ticket(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    form = forms.AddTicketForm(label_suffix='', instance=ticket)
    if request.method == 'POST':
        form = forms.AddTicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket.save()
            return redirect('my_posts')
    return render(request, 'blog/update_ticket.html', {'form': form})


@login_required
def show_my_posts(request):
    my_tickets = models.Ticket.objects.filter(user=request.user)
    return render(request, 'blog/my_posts.html', {'tickets': my_tickets})
