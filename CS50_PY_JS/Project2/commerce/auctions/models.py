from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class auctinListing(models.Model):
    item_name = models.CharField(max_length=3)
    item_image = models.ImageField(upload_to='posts/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.item_name} {self.price} {self.created_at} "

class bids(models.Model):
    pass

class comment(models.Model):
    pass