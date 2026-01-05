from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import (
    register,
    login_view,
    logout_view,
    profile_view,
    send_request,
    accept_request,
    notifications,
    
)

from posts.views import feed, like_post, comment_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('feed/', feed, name='feed'),

    path('profile/<str:username>/', profile_view, name='profile'),

    path('friend-request/<str:username>/', send_request, name='send_request'),

    path('like/<int:post_id>/', like_post, name='like_post'),
    path('comment/<int:post_id>/', comment_post, name='comment_post'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from accounts.views import (
    register, login_view, logout_view,
    profile_view, edit_profile,
    send_request, accept_request, notifications,reject_request,delete_notification,
)

urlpatterns += [
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('notifications/', notifications, name='notifications'),
    path('accept-request/<int:request_id>/', accept_request),
    path('reject-request/<int:request_id>/', reject_request),
    path('delete-notification/<int:note_id>/', delete_notification),
]
from accounts.views import search_users

urlpatterns += [
    path('search/', search_users, name='search_users'),
]
