from django.db import models
from django.contrib.auth.models import User
from .utils import user_directory_path 
from localflavor.in_.models import INStateField
from django.core.validators import RegexValidator


class Location(models.Model):
    address_1 = models.CharField(max_length=200, blank=True)
    address_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = INStateField(verbose_name="State",blank=True, null=True)
    zip_code = models.CharField(
        max_length=6,
        validators=[RegexValidator(regex=r'^\d{6}$', message='Enter a valid 6-digit PIN code')], verbose_name="pin code"
    )
    
    def __str__(self):
        return f'Location {self.id}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username

