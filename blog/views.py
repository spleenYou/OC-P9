from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.db.models import Q

from authentication.models import User
from . import forms, models


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    tickets = sorted(tickets, key=lambda x: x.time_created, reverse=True)
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
    my_tickets = sorted(my_tickets, key=lambda x: x.time_created, reverse=True)
    return render(request, 'blog/my_posts.html', {'tickets': my_tickets})


@login_required
def subscribe(request):
    error_text = None
    if request.method == 'POST':
        try:
            user_to_follow = User.objects.get(username=request.POST.get('username'))
            user_follows = models.UserFollows()
            user_follows.user = request.user
            user_follows.followed_user = user_to_follow
            user_follows.save()
        except User.DoesNotExist:
            error_text = f"L'utilisateur '{request.POST.get('username')}' n'existe pas"
    list_followed_users = models.UserFollows.objects.filter(user=request.user)
    list_users_following_you = models.UserFollows.objects.filter(followed_user=request.user)
    return render(request, 'blog/subscribe.html', {
        'list_followed_users': list_followed_users,
        'list_users_following_you': list_users_following_you,
        'error_text': error_text,
    })


@login_required
def unsubscribe(request, followed_id):
    followed_user = models.UserFollows.objects.filter(id=followed_id)[0]
    if request.method == 'POST':
        followed_user.delete()
        return redirect('subscribe')
    return render(request, 'blog/unsubscribe.html', {'followed_user': followed_user})
