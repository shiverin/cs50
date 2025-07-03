from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timesince import timesince

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    start_bid = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.URLField(blank=True, null=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} at ${self.start_bid} by {self.owner.username}"

class Category(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class Bid(models.Model):
    listing = models.ForeignKey("Listing", on_delete=models.CASCADE, related_name="bids")
    user_bid = models.DecimalField(max_digits=10, decimal_places=2)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    entered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"${self.user_bid} bid on {self.listing.title} by {self.user.username}"

class Comment(models.Model):
    content = models.TextField()
    listing = models.ForeignKey("Listing", on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    typed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({timesince(self.typed_at)} ago): {self.user} said \"{self.content}\""

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist_entries")
    watchlisting=models.ForeignKey("Listing", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} is watching {self.watchlisting}"
