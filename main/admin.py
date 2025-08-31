from django.contrib import admin
from .models import Listing, Likedlisting

class Listing_admin(admin.ModelAdmin):
    readonly_fields = ('id', )
    
class Likedlist(admin.ModelAdmin):
    readonly_fields = ('id', )    
    
admin.site.register(Listing, Listing_admin)
admin.site.register(Likedlisting, Likedlist)
    
    