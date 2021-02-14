from django.contrib import admin

from .models import auctionListings,listingsBids, listingsComments


admin.site.register(auctionListings)
admin.site.register(listingsBids)
admin.site.register(listingsComments)
