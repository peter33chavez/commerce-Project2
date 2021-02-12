from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class auctionListings(models.Model):
    listingID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=4000)
    startingPrice = models.DecimalField(max_digits=10000, decimal_places=2)
    imgUrl = models.URLField(max_length=200, null=True)

    def __str__(self):
        return "$" + str(self.startingPrice)
    
class listingBids(models.Model):
    listingID = models.ForeignKey(related_name=)
    


class listingComments(models.Model):
    pass
#TODO