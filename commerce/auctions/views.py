from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import listingForm

from .models import User, auctionListings



def index(request):
    return render(request, "auctions/index.html")


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

def create_listing(request): 
    if request.user.is_authenticated:
        if request.method == "POST":
            form = listingForm(request.POST)
            if form.is_valid():
                listing = form.save(commit=False)
                listing.user = request.user
                listing.save()
                return render(request, "auctions/create_listing.html", {
                    'message':"Your Listing is now posted"
                })
        else:
            form = listingForm()          
        return render(request, "auctions/create_listing.html", {
            'form':form
        })    


#Active Listings Page 
    #TODO
    #REQUIREMENTS
    #this is shown on the index page 
    #show all current active listings
    #should display at least (the title, description, current price, and photo (if one exists for the listing))

#@login_required
#Listing Page
    #TODO
    #REQUIREMENTS

    #if user is signed in they should be able to "add to WatchList"
    #if item is already in watch list display "remove from watchlist" instead 

    # if signed in user should be able to bid on item with the minimum bid being higher than starting bid or its current else return error "not meeting requirements"

    #if signed in and the listing is yours, the ability to close the listing should be on this page 
    #making the highest bid the winner 
    #listing should no longer be availabe in active listings displayed as "closed listing"

    #if logged in and on a closed listing page and the user was the winning bid. page should display that.

    #if logged in users should be able to add comments to listing at the bottom. 
    #page should display all comments from that specific listing.

#@login_required
#WatchList
    #TODO
    #REQUIREMENTS

    # users who are logged in should have a link on the dashboard for watchlist items. which should display all their watchlist listings. 
    #optional- show active and closed listings

    # clicked on user should be redirected to the listing page. 


#Categories 
    #TODO
    #REQUIREMENTS

    #categories page should show all available categories. and when you select a category you should be brought to search results with that category in listening 
    
    #all results should be clickable 


#Django Admin Interface
    #TODO
    #REQUIREMENTS

    #create a createsuperuser account