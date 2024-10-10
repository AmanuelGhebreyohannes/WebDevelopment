from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, auctionListing
from . import forms


def index(request):
    if request.method == "POST":

        form_input = forms.createListingForm(request.POST)

        if form_input.is_valid():

            new_item_name = form_input.cleaned_data["title"]
            new_item_description = form_input.cleaned_data["description"]
            new_item_price = form_input.cleaned_data["start_bid_value"]
            new_item_image_url = form_input.cleaned_data["image_url"]
            new_item_category = form_input.cleaned_data["category"]
            
            # create a new listing
            newList = auctionListing(
                item_name = new_item_name,
                item_image = new_item_image_url,
                price = new_item_price,
                description = new_item_description,
                category = new_item_category
            )

            # save the new listing
            newList.save()
        
    
    # retrieve all listings

    auctionListings = auctionListing.objects.all()


    return render(request, "auctions/index.html",{'auctionListings':auctionListings})


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
def createListing(request):
    if not User.is_authenticated:
        return render(request, "auctions/login.html")
    if request.method == "POST":
        return render(request, "auctions/index.html")
    #return render(request, "auctions/index.html")
    return render(request,"auctions/createListing.html",{
        'createListingForm':forms.createListingForm
    })


