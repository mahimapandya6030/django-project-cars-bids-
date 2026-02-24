from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Listing, Testdrive
from .serializer import ListingSerializer, Testdriveserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, permissions
from .serializer import ListingSerializer, Testdriveserializer
from .models import Listing
from rest_framework.generics import UpdateAPIView, ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .pagination import Listingpagination
from rest_framework import generics



class ListingListview(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    pagination_class = Listingpagination
    
    
class ListingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def perform_destroy(self, instance):
        # Only the owner can delete
        if instance.seller != self.request.user.profile:
            raise PermissionError("You cannot delete this listing")
        instance.delete()

class ListingUpdateAPIView(UpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def perform_update(self, serializer):
        # Make sure only the owner can update
        if serializer.instance.seller != self.request.user.profile:
            raise PermissionError("You cannot edit this listing")
        serializer.save()
        
        
class ListingCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(seller=request.user.profile)   
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class Testdriveapiview(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = Testdriveserializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user.profile)
            return Response({"messsage": "Test drive booked successfully", "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        
class TestDriveListCreateView(ListCreateAPIView):
    queryset = Testdrive.objects.all()
    serializer_class = Testdriveserializer      
  
class TestDriveRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Testdrive.objects.all()
    serializer_class = Testdriveserializer
    
            
@api_view(['GET', 'POST'])
def listing_api(request):
    if request.method == 'GET':
        listing = Listing.objects.all()
        serializer = ListingSerializer(listing, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ListingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def single_listing_api(request, id):
    listing = Listing.objects.get(id=id)
    serializer = ListingSerializer(listing)
    return Response(serializer.data)


    
      
    
    
    