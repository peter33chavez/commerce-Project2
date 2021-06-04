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
                
                    'message': "Your Listing is now posted"
                })
        else:
            form = listingForm()          
        return render(request, "auctions/create_listing.html", {
            'form':form
        })    




def listing_page(request, listing_id):
    listing = auctionListings.objects.get(pk=listing_id)
    loggedIn = False
    message = None
    if request.user.is_authenticated:
        loggedIn = True
        if request.user in listing.watchers.all():
            wishlisted = True
        else:
            wishlisted = False  
        if request.method == "POST":
            bidForm = BidForm(request.POST)
            commentForm = CommentForm(request.POST)
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
            'message': message,
            'wishlisted': wishlisted
            })
        
        return render(request, "auctions/listing_page.html",{
        'listing': listing,
        'bid_option': BidForm(),
        'comments': listing.get_comments.all(),
        'leave_comment': CommentForm(),
        'loggedIn': loggedIn,
        'wishlisted': wishlisted
        })
    else:    
        return render(request, "auctions/listing_page.html",{
        'listing': listing,
        'comments': listing.get_comments.all(),
        'loggedIn': loggedIn,
        })
    
def update_wishlist(request, listing_id):
    current_listing = auctionListings.objects.get(pk=listing_id)
    if request.user in current_listing.watchers.all():
        current_listing.watchers.remove(request.user)
    else:
        current_listing.watchers.add(request.user)
    return HttpResponseRedirect(reverse('listing_page', args=[listing_id]))    


def listing_status(request, listing_id):
    active_listing = auctionListings.objects.get(pk=listing_id)
    if request.user == active_listing.user:
        if active_listing.topBid:
            active_listing.status = False
            active_listing.buyer = listingsBids.objects.filter(listing_id=active_listing).last().user
            active_listing.save()
            return HttpResponseRedirect(reverse('listing_page', args=[listing_id]))
        else:
            active_listing.status = False
            active_listing.save()
            return HttpResponseRedirect(reverse('listing_page', args=[listing_id]))

def wishlist(request):
    user=request.user
    wishlist_listings= user.watching.all()
    return render(request, 'auctions/wishlist.html',{
        'listings':wishlist_listings
    })



def category_search(request): 
    listings = auctionListings.objects.all()
    if listings:
        allCategories = categories.objects.all()
        return render(request, 'auctions/category_search.html',{
            'categoryList': allCategories
        })
    else:
        return render(request, 'auctions/category_search.html',{
            'message': 'No current listings'
        })


def category_results(request, category):
    category_title = categories.objects.get(pk=category)
    allListings = auctionListings.objects.filter(category=category, status=True).all()
    if allListings:    
        return render(request, 'auctions/category.html',{
        'listings': allListings,
        'category_title': category_title
        })
    else:    
        return render(request, 'auctions/category.html',{
        'message': 'Sorry, no listings under this Category'
        })
    