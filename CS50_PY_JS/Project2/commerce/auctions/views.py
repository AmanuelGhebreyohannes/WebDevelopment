from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max

from .models import User, auctionListing, bids
from . import forms


def index(request):
    error_message = ""
    if request.method == "POST" and request.user.is_authenticated:

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
                category = new_item_category,
                listed_by = request.user.id,
                bid_number = 0
                
            )

            # save the new listing
            newList.save()

        
            
        else:
            error_message = "INVALID INPUT"
            return render(request,"auctions/createListing.html",{
                'createListingForm':forms.createListingForm,
                'error_message':error_message
            })
                    
            

        
    
    # retrieve all listings

    auctionListings = auctionListing.objects.all()


    return render(request, "auctions/index.html",{'auctionListings':auctionListings,'error_message':error_message})


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
    
def createListing(request):
    if not request.user.is_authenticated:
        return render(request, "auctions/login.html")
    if request.method == "POST":         
        # retrieve all listings
        auctionListings = auctionListing.objects.all()
        return render(request, "auctions/index.html",{'auctionListings':auctionListings})
    #return render(request, "auctions/index.html")
    return render(request,"auctions/createListing.html",{
        'createListingForm':forms.createListingForm
    })

def currentListing(request,id):
    watchlisted = False
    if not request.user.is_authenticated:
        return render(request, "auctions/login.html")
    auctionListingItem = None
    if request.method == "GET":
        auctionListingItem = get_object_or_404(auctionListing,pk=id)

    # check if item is already watchlisted
    if(id not in request.user.watchlisted_items):
        watchlisted = False
    else:
        watchlisted = True 

    max_bid = bids.objects.filter(auctionListing_id=auctionListingItem.id).aggregate(Max('bid_amount'))
    max_bid = round(max(float(max_bid['bid_amount__max'])+0.01, float(auctionListingItem.price))+0.01,2)   
    is_creator_of_listing = (get_object_or_404(User,pk=auctionListingItem.listed_by).username == request.user.username)
    #return render(request, "auctions/index.html")
    return render(request,"auctions/currentListing.html",{
        'auctionListing':auctionListingItem,
        # 'PlaceBids':forms.PlaceBids,
        'watchlisted':watchlisted,
        'listedby':get_object_or_404(User,pk=auctionListingItem.listed_by).username,
        'minBid':max_bid,
        'is_creator_of_listing':is_creator_of_listing
    })




def updateWatchlist(request,id):
    watchlisted = False
    if not request.user.is_authenticated:
        return render(request, "auctions/login.html")
    auctionListingItem = None
    if request.method == "GET":
        auctionListingItem = get_object_or_404(auctionListing,pk=id)
        if(id not in request.user.watchlisted_items):
           request.user.watchlisted_items.append(id)
           watchlisted = True
        else:
            request.user.watchlisted_items.remove(id)
            watchlisted = False
        # Save the user instance to persist the changes
        request.user.save()
    max_bid = bids.objects.filter(auctionListing_id=auctionListingItem.id).aggregate(Max('bid_amount'))
    max_bid = round(max(float(max_bid['bid_amount__max']), float(auctionListingItem.price))+0.01,2) 
    is_creator_of_listing = (get_object_or_404(User,pk=auctionListingItem.listed_by).username == request.user.username)

    #return render(request, "auctions/index.html")
    return render(request,"auctions/currentListing.html",{
        'auctionListing':auctionListingItem,
        # 'PlaceBids':forms.PlaceBids,
        'watchlisted':watchlisted,
        'listedby':get_object_or_404(User,pk=auctionListingItem.listed_by).username,
        'minBid':max_bid,
        'is_creator_of_listing':is_creator_of_listing
    })

@login_required
def placeBid(request):
    if request.method == "POST":

        id = request.POST.get("id")
        bid_amount = request.POST.get("bid")

        # create a new listing
        newBid = bids(
            user_id = request.user.id,
            auctionListing_id = id,
            bid_amount = bid_amount,
            
        )

        # save the new listing
        newBid.save()

        # retrieve max bid

        max_bid = bids.objects.filter(auctionListing_id=newBid.auctionListing_id).aggregate(Max('bid_amount'))
        auctionListingItem = get_object_or_404(auctionListing,pk=newBid.auctionListing_id)
        max_bid = round(max(float(max_bid['bid_amount__max']), float(auctionListingItem.price))+0.01,2)
        print(max_bid,bid_amount)
        watchlisted = False
        if(id not in request.user.watchlisted_items):
            watchlisted = False
        else:
            watchlisted = True 
        is_creator_of_listing = (get_object_or_404(User,pk=auctionListingItem.listed_by).username == request.user.username)

        return render(request,"auctions/currentListing.html",{
            'auctionListing':auctionListingItem,
            # 'PlaceBids':forms.PlaceBids,
            'watchlisted':watchlisted,
            'listedby':get_object_or_404(User,pk=auctionListingItem.listed_by).username,
            'minBid': max_bid,
            'is_creator_of_listing':is_creator_of_listing
            })
    

