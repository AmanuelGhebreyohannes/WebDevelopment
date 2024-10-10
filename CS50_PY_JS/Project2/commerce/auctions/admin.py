from django.contrib import admin
from .models import auctionListing

# Register your models here.
@admin.register(auctionListing)
class auctionListingAdmin(admin.ModelAdmin):
    list_display = ("item_name","description")
