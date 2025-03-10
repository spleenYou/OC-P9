"""
URL configuration for LITRevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import blog.views
import authentication.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', authentication.views.login_page, name='login'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('', blog.views.home, name='home'),
    path('logout/', authentication.views.logout_user, name="logout"),
    path('ticket/add/', blog.views.add_ticket, name='add_ticket'),
    path('ticket/<int:ticket_id>/update/', blog.views.update_ticket, name='update_ticket'),
    path('ticket/<int:ticket_id>/del/', blog.views.del_ticket, name='del_ticket'),
    path('ticket/<int:ticket_id>/make_review', blog.views.review_from_ticket, name='review_from_ticket'),
    path('my_posts/', blog.views.show_my_posts, name='my_posts'),
    path('review/add/', blog.views.add_review, name='add_review'),
    path('review/<int:review_id>/update', blog.views.update_review, name='update_review'),
    path('review/<int:review_id>/del', blog.views.del_review, name='del_review'),
    path('subscribe/', blog.views.subscribe, name='subscribe'),
    path('unsubscribe/<int:followed_id>/', blog.views.unsubscribe, name='unsubscribe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
