from django import forms
from .models import auctionListings

class listingForm(forms.ModelForm):
    class Meta:
        model = auctionListings
        fields = ('title','description','startingPrice','imgUrl', 'category')
        labels = { 
            'imgUrl': 'Image Url',
            'startingPrice': 'Starting Price' 
         }
