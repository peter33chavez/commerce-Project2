from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *

from .models import *



def index(request):
    activeListings = auctionListings.objects.all()

    return render(request, "auctions/index.html", {
        'listings': activeListings
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
                listing.user_id = request.user.id
                listing.save()
                return HttpResponseRedirect(reverse( "listing_page", args=[listing.id]),{
                
                    'message':"Your Listing is now posted"
                })
        else:
            form = listingForm()          
        return render(request, "auctions/create_listing.html", {
            'form':form
        })    




def listing_page(request, listing_id):
    listing = auctionListings.objects.get(pk=listing_id)
    loggedIn = False
    if request.user.is_authenticated:
        loggedIn = True
        if request.method == "POST":
            bidForm = BidForm(request.POST)
            commentForm = CommentForm(request.POST)
            #check which form is submitted 
            if bidForm and bidForm.is_valid():
                bid = float(request.POST['bids'])
                #check if this bid is >= or more than top bid.
                if bid >= listing.startingPrice and listing.topBid is None or bid > listing.topBid:
                    bid = bidForm.save(commit=False)
                    bid.user = request.user
                    bid.listing_id = listing
                    bid.save()
                    listing.topBid = bid.bids
                    listing.save()
                    message = 'Your bid has been placed!'
                else:    
                    message = 'Bid is too low.'       
            #allow users to add comments to page
            elif commentForm.is_valid(): 
                comment = commentForm.save(commit=False)
                comment.user = request.user
                comment.listing_id = listing
                comment.save()
                message = 'Comment posted!'
            return render(request, "auctions/listing_page.html",{
            'listing': listing,
            'bid_option': BidForm(),
            'comments': listing.get_comments.all(),
            'leave_comment': CommentForm(),
            'loggedIn': loggedIn,
            'message': message
            })
        
        return render(request, "auctions/listing_page.html",{
        'listing': listing,
        'bid_option': BidForm(),
        'comments': listing.get_comments.all(),
        'leave_comment': CommentForm(),
        'loggedIn': loggedIn
        })
    else:    
        return render(request, "auctions/listing_page.html",{
        'listing': listing,
        'comments': listing.get_comments.all(),
        'loggedIn': loggedIn,
        })
    

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