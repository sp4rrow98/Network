from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import json
from .models import User, Post, Followers, Likes



def index(request):
    if request.method == "GET":
        posts = Post.objects.order_by('-timestamp')
        paginator = Paginator(posts, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "network/index.html", {
            "posts": posts,
            "page_obj": page_obj,
        })


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required(login_url='login')
def new_post(request):
    if request.method == "GET":
        # Render Page
        return render(request, "network/new_post.html")
    else:
        # Get POST data from the user
        description = request.POST["description"]
        # photo = request.POST["photo"]
        # Update db
        obj = Post(description=description, owner=request.user)
        obj.save()
        return HttpResponseRedirect(reverse('index'))

@login_required(login_url='login')
def profile(request, user):
    if request.method == "GET":
        current_user = request.user
        owner = User.objects.get(username=user)
        is_following = Followers.objects.filter(follower=owner).count()
        is_follower = Followers.objects.filter(following = owner, follower=current_user)
        follow_count = Followers.objects.filter(following=owner).count()
        posts = Post.objects.filter(owner=owner).order_by("-timestamp")
        paginator = Paginator(posts, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "network/profile.html", {
            "owner": owner,
            "current_user" : current_user,
            "followers" : is_follower,
            "posts": posts,
            "page_obj": page_obj,
            "follow_count": follow_count,
            "is_following_count": is_following
        })

    if request.method == "POST":
        # Following
        if request.POST.get('follow'):
            follower = request.POST["follow"]
            follower_user = User.objects.get(username=follower)
            user_id = User.objects.get(username=user)
            new_follower = Followers(follower=follower_user, following=user_id)
            new_follower.save()
            return HttpResponseRedirect(reverse('profile', args=[user]))
        # Unfollowing
        if request.POST.get('unfollow'):
            unfollow = request.POST["unfollow"]
            unfollower_user = User.objects.get(username=unfollow)
            user_id = User.objects.get(username=user)
            remove_follower = Followers.objects.filter(follower=unfollower_user, following=user_id)
            remove_follower.delete()
            return HttpResponseRedirect(reverse('profile', args=[user]))


@login_required(login_url='login')
def following(request):
    if request.method == "GET":
        follows = Followers.objects.filter(follower=request.user).values_list('following')
        posts = Post.objects.filter(owner__in = follows).order_by("-timestamp")
        paginator = Paginator(posts, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "network/following.html", {
            "posts" : posts,
            "page_obj": page_obj
        })


@login_required(login_url='login')
def edit(request, id):
    if request.method == "POST":
        post = Post.objects.get(id=id, owner=request.user)
        data = json.loads(request.body)
        if len(data.get("description", " ")) <= 0:
            return JsonResponse({"message": "Posts cannot be empty"})
        post.description = data.get("description")
        post.save()
        return JsonResponse({"saved": True}, status=200)

@login_required(login_url='login')
def like(request, id):
    if request.method == "PATCH":
        user = request.user
        post = Post.objects.get(id=id)
        data = json.loads(request.body)
        likes = data.get("likes")
        like = Likes.objects.filter(post=id, likes=user)
        if like:
            post.likes = post.likes - 1
            post.save()
            like.delete()
            count = Post.objects.get(id=id)
            return JsonResponse(count.serialize())
        else:
            post.likes = likes + 1
            post.save()
            like = Likes(post=post, likes=user)
            like.save()
            count = Post.objects.get(id=id)
            return JsonResponse(count.serialize())