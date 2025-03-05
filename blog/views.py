from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from itertools import chain

from authentication.models import User
from . import forms, models


@login_required
def home(request):
    """
    Shows the tickets and review made by login user and followed users, review from other users in reply to login user

    Args:
        request (HttpRequest): HttpRequest

    Returns:
        HttpRequest: Return the home page
    """
    followed_users = models.UserFollows.objects.filter(user=request.user)
    followed_users = list(followed_user.followed_user for followed_user in followed_users)
    my_tickets = models.Ticket.objects.filter(user=request.user)
    followed_users_tickets = models.Ticket.objects.filter(user__in=followed_users)
    reviews = models.Review.objects.filter(Q(user=request.user) | Q(user__in=followed_users) | Q(ticket__in=my_tickets))
    posts = sorted(chain(my_tickets, followed_users_tickets, reviews), key=lambda x: x.time_created, reverse=True)
    return render(request, 'blog/home.html', {
        'posts': posts,
        'rating_range': range(5),
    })


@login_required
def add_ticket(request):
    """
    Shows the page to add a new ticket

    Args:
        request (HttpRequest): HttpRequest

    Returns:
        HttpRequest: Return the add ticket page
    """
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
    """
    Shows the page to delete a ticket and ask for it

    Args:
        request (HttpRequest): HttpRequest
        ticket_id (int): Ticket's id to delete

    Returns:
        HttpRequest: Return the delete page for ticket
    """
    ticket = models.Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('my_posts')
    return render(request, 'blog/del_ticket.html', {'ticket': ticket})


@login_required
def update_ticket(request, ticket_id):
    """
    Shows the page to update a ticket

    Args:
        request (HttpRequest): HttpRequest
        ticket_id (int): Ticket's id to update

    Returns:
        HttpRequest: Return the update page for ticket
    """
    ticket = models.Ticket.objects.get(id=ticket_id)
    form = forms.AddTicketForm(label_suffix='', instance=ticket)
    if request.method == 'POST':
        form = forms.AddTicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket.title = request.POST.get('title')
            ticket.description = request.POST.get('description')
            if request.FILES.get('image'):
                ticket.image = request.FILES.get('image')
            if request.POST.get('clear_image'):
                ticket.image = None
            ticket.save()
            return redirect('my_posts')
    return render(request, 'blog/update_ticket.html', {'form': form})


@login_required
def review_from_ticket(request, ticket_id):
    """
    Shows the page to made a review from a ticket

    Args:
        request (HttpRequest): HttpRequest
        ticket_id (int): Ticket's id to reply

    Returns:
        HttpRequest: Return the review page from ticket
    """
    ticket = models.Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        data_review = {
            'body': request.POST.get('body'),
            'rating': int(request.POST.get('rating')),
            'headline': request.POST.get('headline'),
        }
        form_review = forms.AddReviewForm(data_review)
        if form_review.is_valid():
            review = form_review.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    form_review = forms.AddReviewForm(label_suffix='')
    return render(request, 'blog/review_from_ticket.html', {'post': ticket, 'form_review': form_review})


@login_required
def show_my_posts(request):
    """
    Shows user's tickets and reviews

    Args:
        request (HttpRequest): HttpRequest

    Returns:
        HttpRequest: Return the user's tickets and reviews page
    """
    my_tickets = models.Ticket.objects.filter(user=request.user)
    my_reviews = models.Review.objects.filter(user=request.user)
    my_posts = sorted(chain(my_tickets, my_reviews), key=lambda x: x.time_created, reverse=True)
    return render(request, 'blog/my_posts.html', {
        'posts': my_posts,
        'allow_modification': True,
        'rating_range': range(5),
    })


@login_required
def subscribe(request):
    """
    Shows the page to create an account

    Args:
        request (HttpRequest): HttpRequest

    Returns:
        HttpRequest: Return the suscribe page
    """
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
    """
    Shows the page to delete an account

    Args:
        request (HttpRequest): HttpRequest

    Returns:
        HttpRequest: Return the unsuscribe page
    """
    followed_user = models.UserFollows.objects.filter(id=followed_id)[0]
    if request.method == 'POST':
        followed_user.delete()
        return redirect('subscribe')
    return render(request, 'blog/unsubscribe.html', {'followed_user': followed_user})


@login_required
def add_review(request):
    """
    Shows the page to add review from nothing

    Args:
        request (HttpRequest): HttpRequest

    Returns:
        HttpRequest: Return the page to add review from nothing
    """
    if request.method == 'POST':
        form_ticket = forms.AddTicketForm(request.POST, request.FILES)
        data_review = {
            'body': request.POST.get('body'),
            'rating': int(request.POST.get('rating')),
            'headline': request.POST.get('headline'),
        }
        form_review = forms.AddReviewForm(data_review)
        if form_ticket.is_valid() and form_review.is_valid():
            ticket = form_ticket.save(commit=False)
            ticket.user = request.user
            review = form_review.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            ticket.save()
            review.save()
            return redirect('home')
    form_ticket = forms.AddTicketForm(label_suffix='')
    form_review = forms.AddReviewForm(label_suffix='')
    return render(request, 'blog/add_review.html', {'form_review': form_review, 'form_ticket': form_ticket})


@login_required
def update_review(request, review_id):
    """
    Shows the page to update a review

    Args:
        request (HttpRequest): HttpRequest
        review_id: review's id to update

    Returns:
        HttpRequest: Return the page to update a review
    """
    review = models.Review.objects.get(id=review_id)
    if request.method == 'POST':
        form_review = forms.AddReviewForm(request.POST)
        if form_review.is_valid():
            review.headline = request.POST.get('headline')
            review.rating = request.POST.get('rating')
            review.body = request.POST.get('body')
            review.save()
            return redirect('my_posts')
    form_review = forms.AddReviewForm(instance=review)
    return render(request, 'blog/update_review.html', {
        'form_review': form_review,
        'post': review,
        'rating_range': range(5),
    })


@login_required
def del_review(request, review_id):
    """
    Shows the page to delete a review

    Args:
        request (HttpRequest): HttpRequest
        review_id: review's id to delete

    Returns:
        HttpRequest: Return the page to delete a review
    """
    review = models.Review.objects.get(id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('my_posts')
    return render(request, 'blog/del_review.html', {'review': review})
