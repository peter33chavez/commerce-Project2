from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
 

    def __str__(self):
        return f"{self.username}"
        
class categories(models.Model):

    category = models.CharField(max_length=200) 

    def __str__(self):
        return self.category  

class auctionListings(models.Model):

    title = models.CharField( null=True, max_length=80)
    description = models.TextField(null=True, max_length=4000)
    startingPrice = models.FloatField(null=True,)
    imgUrl = models.URLField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(categories, on_delete=models.CASCADE, null=True, related_name='all_listings')
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='my_listings')
    topBid = models.FloatField(null=True, blank=True,)
    buyer = models.ForeignKey(User, null=True, blank=True, max_length=80, on_delete=models.PROTECT, related_name='bought_listings')
    status = models.BooleanField(null=True, default=True)
    watchers = models.ManyToManyField(User, blank=True, related_name='watching')

    def __str__(self):
        return self.title

class listingsBids(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bids = models.FloatField()
    listing_id = models.ForeignKey(auctionListings, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Bid:${self.bids} by {self.user}"
    

class listingsComments(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.CharField(max_length=80)
    listing_id = models.ForeignKey(auctionListings, on_delete=models.CASCADE, null=True, related_name='get_comments')

    def __str__(self):
        return f"{self.user.username}"