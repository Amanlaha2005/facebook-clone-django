from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Like, Comment

from accounts.models import FriendRequest

@login_required
def feed(request):

    # CREATE POST
    if request.method == 'POST':
        Post.objects.create(
            user=request.user,
            content=request.POST.get('content'),
            image=request.FILES.get('image')
        )
        return redirect('feed')

    # ----------------------------
    # FRIENDS-ONLY FEED LOGIC
    # ----------------------------

    # users whom I sent request AND accepted
    sent_friends = FriendRequest.objects.filter(
        sender=request.user,
        is_accepted=True
    ).values_list('receiver_id', flat=True)

    # users who sent me request AND accepted
    received_friends = FriendRequest.objects.filter(
        receiver=request.user,
        is_accepted=True
    ).values_list('sender_id', flat=True)

    # combine friend IDs safely
    friend_ids = list(sent_friends) + list(received_friends)

    # include my own posts
    friend_ids.append(request.user.id)

    # fetch posts
    posts = Post.objects.filter(
        user_id__in=friend_ids
    ).order_by('-created_at')

    return render(request, 'feed.html', {'posts': posts})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        like.delete()   # toggle like

    return redirect('feed')
@login_required
def comment_post(request, post_id):
    Comment.objects.create(
        user=request.user,
        post_id=post_id,
        text=request.POST['comment']
    )
    return redirect('feed')
