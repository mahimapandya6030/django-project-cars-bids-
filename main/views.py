from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Listing, Likedlisting
from user.models import Profile, Location
from .forms import ListingForm
from user.forms import LocationForm
from django.contrib import messages
from .filters import ListingFilter
from django import views
from django.shortcuts import get_object_or_404
from user.forms import Userform, Profileform, LocationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.mail import send_mail
from django.http import HttpResponse

def main(request):
    return render(request, "design/main.html")

@login_required
def home(request):
    listing = Listing.objects.all()
    listing_filters = ListingFilter(request.GET, queryset=listing)
    context = {
        'listing' : listing,
        'listing_filter': listing_filters,
    }
    return render(request, 'design/home.html', context)


@login_required
def list_view(request):
    if request.method == 'POST':
        try:
            listing_form = ListingForm(request.POST, request.FILES)
            location_form = LocationForm(request.POST)
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
                listing.location = listing_location
                listing.save()
                messages.info(request, f"{listing.model} is successfully added.")
                return redirect('home') 
            else:
                raise Exception()   
        except Exception as e:
            print(e)
            messages.error(request, "error occured while posting")  
                
    elif request.method == 'GET':
        listing_form = ListingForm()
        location_form = LocationForm()
    return render(request, 'components/list.html', {'listing_form': listing_form, 'location_form': location_form})    
    
        
def listing_view(request, id):
    try:
        listing = Listing.objects.filter(id=id).first()
    except:
        return HttpResponse("listing not found")
    return render(request, 'components/listing.html', {'listing':listing})


def edit_view(request, id):
    listing = get_object_or_404(Listing, id=id)
    if request.method == 'POST':
        user_form = Userform(request.POST, instance=request.user)
        location_form = LocationForm(request.POST,request.FILES, instance=request.user.profile.location)
        profile_form = Profileform(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and location_form.is_valid() and profile_form.is_valid():
            user_form.save()
            location_form.save()
            profile_form.save()
            messages.success(request, 'profile updated.')
            return redirect('home')
        else:
            messages.error(request, 'Update failed. Please check the form.')    
    else:
        # Prefill forms with data on GET request
        user_form = Userform(instance=request.user)
        location_form = LocationForm(instance=request.user.profile.location)
        profile_form = Profileform(instance=request.user.profile)        
    return render(request, 'components/edit.html', {'user_form': user_form, 
                                                    'location_form': location_form, 
                                                    'profile_form': profile_form})    
    
    
@login_required    
def like_listing_view(request, id):
    listing = get_object_or_404(Listing, id=id)

    liked_listing, created = Likedlisting.objects.get_or_create(
        profile=request.user.profile, listing=listing)

    if not created:
        liked_listing.delete()
    else:
        liked_listing.save()

    return JsonResponse({
        'is_liked_by_user': created,
    })


def send_test_email(request, id):
    listing = get_object_or_404(Listing, id=id) 
    try: 
        send_mail(
            'Car Marketplace Update',
            'Your car has been successfully posted!',
            'mahimapandya6030@gmail.com',
            [ listing.seller.user.email ],
            fail_silently=False,
        )    
        return JsonResponse({
            "success": True,
        })
    except Exception as e:
        print(e)    
        return JsonResponse({
            "success": False,
            "info": e,
        })