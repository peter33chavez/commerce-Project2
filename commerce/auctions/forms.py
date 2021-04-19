from django import forms
from .models import auctionListings

class listingForm(forms.ModelForm):
    class Meta:
        model = auctionListings
        fields = ('title','description','startingPrice','imgUrl', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-box bg-dark'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-box bg-dark'}),
            'startingPrice': forms.NumberInput(attrs={'class': 'form-control form-box bg-dark'}),
            'imgUrl': forms.TextInput(attrs={'class': 'form-control form-box bg-dark'}),
            'category': forms.Select(attrs={'class': 'form-control form-box bg-dark'})
        }
        labels = { 
            'imgUrl': 'Image Url',
            'startingPrice': 'Starting Price' 
         }

