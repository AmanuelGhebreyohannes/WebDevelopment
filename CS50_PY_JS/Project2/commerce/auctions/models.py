from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    watchlisted_items = models.JSONField(default=list)
    pass

class auctionListing(models.Model):
    item_name = models.CharField(max_length=100)
    item_image = models.ImageField(upload_to='posts/')
    description = models.CharField(max_length=500,default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    active_status = models.BooleanField(default=True)
    category = models.CharField(max_length=100, default="")
    listed_by = models.CharField(max_length=100, default="")
    bid_number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item_name} {self.price} {self.active_status} {self.description} {self.created_at} {self.item_image} {self.category} "

class bids(models.Model):
    pass

class comment(models.Model):
    pass