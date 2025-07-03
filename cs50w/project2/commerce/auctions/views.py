from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User
from .models import Listing, Bid, Comment, Category, Watchlist
from django.db.models import Max, F, Value, Subquery, OuterRef
from django.db.models.functions import Coalesce
from decimal import Decimal

def index(request):
    listings = Listing.objects.annotate(
        highest_bid=Max('bids__user_bid')
    ).annotate(
        current_price=Coalesce('highest_bid', F('start_bid'))
    ).filter(is_active=True)
    context = {
        "listings": listings
    }
    return render(request, "auctions/index.html", context)

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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    if request.method=="POST":
        title=request.POST["title"]
        description=request.POST["body"]
        bid=request.POST["bid"]
        url=request.POST["url"]
        cat=request.POST["category"]
        if cat:
            cat_id=Category.objects.get(name=cat)
        else:
            cat_id=None
        listing = Listing(
            title=title,
            description=description,
            start_bid=bid,
            url=url,
            category=cat_id,
            owner=request.user
        )
        listing.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,"auctions/create.html")

@login_required
def watch(request):
    user = request.user
    listings = Watchlist.objects.filter(user=user)
    return render(request,"auctions/watch.html",{
        "listings":listings,
    })


def listings(request, id):
    highest_bidder_subquery = Bid.objects.filter(
        listing=OuterRef('pk')
    ).order_by('-user_bid', 'entered_at').values('user__username')[:1]

    listings = Listing.objects.annotate(
        highest_bid=Max('bids__user_bid'),
        current_price=Coalesce(Max('bids__user_bid'), F('start_bid')),
        highest_bid_username=Subquery(highest_bidder_subquery)
    ).get(id=id)
    is_watched = False
    current_price = Decimal(listings.current_price)
    if request.user.is_authenticated:
        is_watched = Watchlist.objects.filter(user=request.user, watchlisting=id).exists()
    if request.method=="POST":
        listing_id=request.POST["listing_id"]
        if "bid" in request.POST:
            newbid=Decimal(request.POST["bid"])
            if current_price==listings.start_bid and newbid<current_price:
                messages.error(request, "Your bid must be higher or equal to the starting bid.")
                return HttpResponseRedirect(reverse("listings",args=[listing_id]))
            elif newbid<=current_price:
                messages.error(request, "Your bid must be higher than the current highest bid.")
                return HttpResponseRedirect(reverse("listings",args=[listing_id]))
            else:
                bid = Bid(
                    listing=listings,
                    user_bid=newbid,
                    user=request.user,
                )
                bid.save()
        if "comment" in request.POST:
            newcomment=request.POST["comment"]
            comment = Comment(
                        content= newcomment,
                        listing=listings,
                        user=request.user,
                    )
            comment.save()
        elif "close_auction" in request.POST:
                if request.user == listings.owner:
                    listings.is_active = False
                    listings.save()
                else:
                    messages.error(request, "Only the owner can close the auction.")
                return HttpResponseRedirect(reverse("listings",args=[listing_id]))
        if not "comment" in request.POST and not "bid" in request.POST:
            watch_entry = Watchlist.objects.filter(user=request.user, watchlisting=listings)
            if watch_entry.exists():
                watch_entry.delete()
            else:
                Watchlist.objects.create(user=request.user, watchlisting=listings)
        return HttpResponseRedirect(reverse("listings",args=[listing_id]))
    else:
        comments=Comment.objects.filter(listing=id)
        if not listings.is_active:
            winning_bid = Bid.objects.filter(listing=listings).order_by("-user_bid").first()
            if winning_bid:
                if winning_bid.user==request.user:
                    messages.success(request, f"Auction closed. You won with a bid of ${winning_bid.user_bid}")
                else:
                    messages.success(request, f"Auction closed. Winner: {winning_bid.user.username} with a bid of ${winning_bid.user_bid}")
            else:
                messages.info(request, "Auction closed with no bids.")
        return render(request, "auctions/listings.html",{
            "listing":listings,
            "comments":comments,
            "is_watched":is_watched,
            })

def categories(request):
    cats=Category.objects.all()
    return render(request, "auctions/categories.html",{
        "categories":cats
    })

def cat(request,catname):
    catid= Category.objects.get(name=catname)
    listings = Listing.objects.filter(category=catid, is_active=True).annotate(
        highest_bid=Max('bids__user_bid'),
        current_price=Coalesce(Max('bids__user_bid'), F('start_bid'))
    )

    return render(request, "auctions/cat.html", {
        "listings": listings,
        "catname": catname,
    })

def archive(request):
    highest_bid_subquery = Bid.objects.filter(
        listing=OuterRef('pk')
    ).order_by('-user_bid', 'entered_at').values('entered_at')[:1]

    listings = Listing.objects.annotate(
        highest_bid=Max('bids__user_bid')
    ).annotate(
        current_price=Coalesce('highest_bid', F('start_bid')),
        highest_bid_entered_at=Subquery(highest_bid_subquery)
    ).filter(is_active=False)
    context = {
        "listings": listings
    }
    return render(request, "auctions/archive.html", context)
