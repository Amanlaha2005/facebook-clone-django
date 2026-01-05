from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile , FriendRequest,Notification
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('feed')
    return render(request, 'login.html')

@login_required
def search_users(request):
    query = request.GET.get('q')
    users = []

    if query:
        users = User.objects.filter(username__icontains=query)

    return render(request, 'search.html', {
        'users': users,
        'query': query
    })
    
    
@login_required
def send_request(request, username):
    receiver = User.objects.get(username=username)

    friend_request, created = FriendRequest.objects.get_or_create(
        sender=request.user,
        receiver=receiver
    )

    if created:
        Notification.objects.create(
            user=receiver,   # ✅ FIXED
            message=f"{request.user.username} sent you a friend request",
            friend_request=friend_request
        )

    return redirect('profile', username=receiver.username)
@login_required
def accept_request(request, request_id):
    fr = get_object_or_404(FriendRequest, id=request_id, receiver=request.user)
    fr.is_accepted = True
    fr.save()

    Notification.objects.create(
        user=fr.sender,
        message=f"{request.user.username} accepted your friend request"
    )

    return redirect('notifications')


@login_required
def reject_request(request, request_id):
    fr = get_object_or_404(FriendRequest, id=request_id, receiver=request.user)
    fr.delete()
    return redirect('notifications')



@login_required
def notifications(request):
    notes = Notification.objects.filter(user=request.user).order_by('-created_at')

    # auto mark as read when page opens
    notes.filter(is_read=False).update(is_read=True)

    return render(request, 'notifications.html', {'notes': notes})


@login_required
def delete_notification(request, note_id):
    note = get_object_or_404(Notification, id=note_id, user=request.user)
    note.delete()
    return redirect('notifications')

@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user)

    is_friend = FriendRequest.objects.filter(
        sender=request.user, receiver=user, is_accepted=True
    ).exists() or FriendRequest.objects.filter(
        sender=user, receiver=request.user, is_accepted=True
    ).exists()

    request_sent = FriendRequest.objects.filter(
        sender=request.user, receiver=user
    ).exists()

    return render(request, 'profile.html', {
        'profile': profile,
        'is_friend': is_friend,
        'request_sent': request_sent
    })

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        profile.bio = request.POST.get('bio')
        if request.FILES.get('profile_pic'):
            profile.profile_pic = request.FILES.get('profile_pic')
        profile.save()
        return redirect('profile', username=request.user.username)

    return render(request, 'edit_profile.html', {'profile': profile})
def logout_view(request):
    logout(request)
    return redirect('login')
