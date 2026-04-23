from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator
from .forms import Userform, Profileform, LocationForm
from main.models import Listing, Likedlisting

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method  == 'POST' and form.is_valid():
        print("POST data received.")
        user = form.get_user()
        login(request, user)
        messages.success(request, "you have logged successfully.")
        return redirect('home')     
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form':form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('main')
    
@method_decorator(login_required, name="dispatch")
class Profileview(View):
    def get(self, request):
        user_listing = Listing.objects.filter(seller=request.user.profile)
        user_liked_listings = Likedlisting.objects.filter(
            profile=request.user.profile).all()
        user_form = Userform(instance=request.user)
        profile_form = Profileform(instance=request.user.profile)
        location_form = LocationForm(instance=request.user.profile.location)
        
        return render(request, 'user/profile.html', {'user_form': user_form, 
                                                     'profile_form': profile_form, 
                                                     'location_form': location_form,
                                                     'user_listing': user_listing,
                                                     'user_liked_listings':user_liked_listings})    
    def post(self, request):
        user_listing = Listing.objects.filter(seller=request.user.profile)
        user_liked_listings = Likedlisting.objects.filter(
            profile=request.user.profile).all()
        user_form = Userform(request.POST, instance=request.user)    
        profile_form = Profileform(request.POST, request.FILES, instance=request.user.profile)
        location_form = LocationForm(request.POST, instance=request.user.profile.location)
       
        if user_form.is_valid() and profile_form.is_valid() and location_form.is_valid():
            user_form.save()
            profile_form.save()
            location_form.save()
            messages.success(request, "you have successfully updated your profile.")
        else:
            messages.error(request, 'ERROR updating profile.')
        return render(request, 'user/profile.html', {'user_form': user_form,
                                                     'profile_form': profile_form, 
                                                     'location_form': location_form,
                                                     'user_listing': user_listing,
                                                     'user_liked_listings':user_liked_listings})
        
        