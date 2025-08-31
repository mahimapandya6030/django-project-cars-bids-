from dataclasses import field
from django import forms
from .models import Location, Profile
from django.contrib.auth.models import User
from .widgets import CustomPictureImageFieldWidget

#custom form
class Userform(forms.ModelForm):
    username = forms.CharField(disabled=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    
    
class Profileform(forms.ModelForm):
    # photo = forms.ImageField(widget=CustomPictureImageFieldWidget())
    bio = forms.TextInput()    
    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'phone_number')
        widgets = {
            'photo': CustomPictureImageFieldWidget()
        }
        
    
class LocationForm(forms.ModelForm):

    address_1 = forms.CharField(required=True)

    class Meta:
        model = Location
        fields = {'address_1', 'address_2', 'city', 'state', 'zip_code'}