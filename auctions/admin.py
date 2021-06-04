from django.contrib import admin

from .models import *


admin.site.register(auctionListings)
admin.site.register(listingsBids)
admin.site.register(listingsComments)
admin.site.register(categories)
