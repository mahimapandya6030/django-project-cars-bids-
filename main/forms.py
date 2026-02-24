from django import forms
from .models import Listing, Testdrive

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = {'brand', 'model', 'vin', 'milege',
                  'color', 'description', 'engine', 'transmission', 'image'}
        
        
        
        
class TestDriveForm(forms.ModelForm):
    class Meta:
        model = Testdrive
        fields = ['date', 'time']        