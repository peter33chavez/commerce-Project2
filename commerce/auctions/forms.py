from django import forms
from .models import auctionListings

class listingForm(forms.ModelForm):
    class Meta:
        model = auctionListings
        widgets = {
            'description': forms.TextInput(attrs={'class': 'new-listing-description'})
        }
        fields = ('title','description','startingPrice','imgUrl', 'category')
        labels = { 
            'imgUrl': 'Image Url',
            'startingPrice': 'Starting Price' 
         }

