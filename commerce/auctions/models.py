from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
 

    def __str__(self):
        return f"{self.username}"
    
class auctionListings(models.Model):
    options = (
        ('Books', 'Books'),
        ('Business & Industrial', 'Business & Industrial'),
        ('Clothing, Shoes & Accessories', 'Clothing, Shoes & Accessories'),
        ('Collectibles', 'Collectibles'),
        ('Consumer Electronics', 'Consumer Electronics'),
        ('Crafts', 'Crafts'),
        ('Dolls & Bears', 'Dolls & Bears'),
        ('Home & Garden', 'Home & Garden'),
        ('Motors', 'Motors'),
        ('Pet Supplies', 'Pet Supplies'),
        ('Sporting Goods', 'Sporting Goods'),
        ('Sports Mem, Cards & Fan Shop', 'Sports Mem, Cards & Fan Shop'),
        ('Toys & Hobbies', 'Toys & Hobbies'),
        ('Antiques', 'Antiques'),
        ('Computers/Tablets & Networking','Computers/Tablets & Networking'),
        ('Other','Other')
    )
    title = models.CharField( null=True, max_length=80)
    description = models.TextField(null=True, max_length=4000)
    startingPrice = models.FloatField(null=True,)
    imgUrl = models.URLField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, choices=options)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    topBid = models.FloatField(null=True, blank=True,)
    status = models.BooleanField(null=True)
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