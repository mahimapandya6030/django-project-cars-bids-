from django.db import models
import uuid
from user.models import Profile, Location
from .consts import CARS_BRANDS, TRANSMISSION_OPTIONS
from .utils import user_Listing_attr

class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    brand = models.CharField(max_length=77, choices=CARS_BRANDS, default=None)
    model = models.CharField(max_length=77)
    vin = models.CharField(max_length=17)
    milege = models.IntegerField(default=0)
    color = models.CharField(max_length=74)
    description = models.TextField()
    engine = models.CharField(max_length=30)
    transmission = models.CharField(max_length=30, choices=TRANSMISSION_OPTIONS, default=None)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=user_Listing_attr)
    
    def __str__(self):
        return f'{self.seller.user.username}\'s Listing - {self.model}'
    
class Likedlisting(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)    
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    like_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return super().__str__()+ f' - {self.listing.model} liked by {self.profile.user.username}'
    