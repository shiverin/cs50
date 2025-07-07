from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator
from .models import User, Post, Like
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Exists, OuterRef
import json


def index(request):
    if request.method == "POST":
        body = request.POST.get("content", "").strip()
        if body:
            post = Post(user=request.user, body=body)
            post.save()
        return redirect('index')

    allposts = Post.objects.all().order_by('-timestamp')
    allposts = allposts.annotate(likes_count=Count('likes'))

    if request.user.is_authenticated:
        user_likes = Like.objects.filter(user=request.user, post=OuterRef('pk'))
        allposts = allposts.annotate(liked=Exists(user_likes))

    paginator = Paginator(allposts, 10)
    pagenumber = request.GET.get('page')
    post = paginator.get_page(pagenumber)

    return render(request, "network/index.html", {
        "posts": post
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


@login_required
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


@login_required
def following(request):
    followed_users = request.user.following.all()
    allposts = Post.objects.filter(user__in=followed_users).order_by('-timestamp')
    allposts = allposts.annotate(likes_count=Count('likes'))

    if request.user.is_authenticated:
        user_likes = Like.objects.filter(user=request.user, post=OuterRef('pk'))
        allposts = allposts.annotate(liked=Exists(user_likes))

    paginator = Paginator(allposts, 10)
    pagenumber = request.GET.get('page')
    posts = paginator.get_page(pagenumber)

    return render(request, "network/following.html", {
        "posts": posts
    })


def profile(request, username):
    profile = get_object_or_404(User, username=username)
    allposts = Post.objects.filter(user=profile).order_by('-timestamp')
    allposts = allposts.annotate(likes_count=Count('likes'))

    if request.user.is_authenticated:
        user_likes = Like.objects.filter(user=request.user, post=OuterRef('pk'))
        allposts = allposts.annotate(liked=Exists(user_likes))

    paginator = Paginator(allposts, 10)
    pagenumber = request.GET.get('page')
    posts = paginator.get_page(pagenumber)

    is_following = False
    if request.user.is_authenticated:
        is_following = profile.followers.filter(id=request.user.id).exists()

    return render(request, "network/profile.html", {
        "profile": profile,
        "posts": posts,
        "is_following": is_following
    })


@login_required
def toggle_like(request, post_id):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    user = request.user
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    like_obj = Like.objects.filter(user=user, post=post).first()
    if like_obj:
        like_obj.delete()
        liked = False
    else:
        Like.objects.create(user=user, post=post)
        liked = True

    likes_count = post.likes.count()
    return JsonResponse({
        "liked": liked,
        "likes_count": likes_count,
    })


@login_required
def toggle_follow(request, username):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    try:
        target_user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found."}, status=404)

    if request.user == target_user:
        return JsonResponse({"error": "Cannot follow yourself."}, status=400)

    if target_user in request.user.following.all():
        request.user.following.remove(target_user)
        is_following = False
    else:
        request.user.following.add(target_user)
        is_following = True

    follower_count = target_user.followers.count()

    return JsonResponse({
        "is_following": is_following,
        "follower_count": follower_count,
    })


@login_required
def edit(request, post_id):
    if request.method != "PUT":
        return JsonResponse({"error": "PUT request required."}, status=400)

    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return HttpResponseNotFound("Post not found.")

    if request.user != post.user:
        return HttpResponseForbidden("You cannot edit this post.")

    data = json.loads(request.body)
    new_body = data.get("body", "").strip()

    if not new_body:
        return JsonResponse({"error": "Post body cannot be empty."}, status=400)

    post.body = new_body
    post.save()

    return JsonResponse({
        "message": "Post updated successfully.",
        "post_id": post_id,
        "new_body": new_body,
    })
