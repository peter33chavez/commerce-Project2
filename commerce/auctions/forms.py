from django import forms
from .models import *

class listingForm(forms.ModelForm):
    class Meta:
        model = auctionListings
        fields = ('title','description','startingPrice','imgUrl', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-box bg-dark'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-box bg-dark'}),
            'startingPrice': forms.NumberInput(attrs={'class': 'form-control form-box bg-dark'}),
            'imgUrl': forms.TextInput(attrs={'class': 'form-control form-box bg-dark', 'placeholder': '*optional*'}),
            'category': forms.Select(attrs={'class': 'form-control form-box bg-dark'})
        }
        labels = { 
            'imgUrl': 'Image Url',
            'startingPrice': 'Starting Price' 
         }

class BidForm(forms.ModelForm):
    class Meta:
        model = listingsBids
        fields = ('bids',)
        widgets={
            'bids': forms.NumberInput(attrs={'class':'form-control bid-form-box bg-dark'})
        }
        labels={
            'bids': ''
        }

class commentForm(forms.ModelForm):
    class Meta:
        model = listingsComments
        fields = ('comments',)
        widgets={
            'comments': forms.CharField(attrs={ 'class':'form-control leave-comment bg-dark', 'placeholder': 'Add a Comment'})
        }
        labels={
            'comments': ''
        }
