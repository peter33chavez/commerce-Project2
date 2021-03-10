from django import forms
from .models import auctionListings

class new_listing(forms.ModelForm):
    class Meta:
        model = auctionListings
        fields = '__all__'
        widgets = {'users_id':forms.HiddenInput()}
