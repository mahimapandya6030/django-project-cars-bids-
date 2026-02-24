from rest_framework import serializers
from .models import Listing, Likedlisting, Testdrive
from user.models import Profile, Location

class ListingSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    
    seller = serializers.StringRelatedField()
    location = serializers.StringRelatedField()
    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ['seller']
        
        
class Testdriveserializer(serializers.ModelSerializer):
    class Meta:
        model = Testdrive 
        fields = ['id', 'listing', 'user', 'date', 'time', 'created_at']
        read_only_fields = ['user'] 
              