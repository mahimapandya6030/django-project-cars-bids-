from django.contrib import admin
from django.urls import path, include
from . import views
from uuid import UUID
from .api_views import ListingCreateAPIView   
from .api_views import ListingUpdateAPIView
from .api_views import ListingRetrieveUpdateDestroyAPIView

from rest_framework.routers import DefaultRouter


urlpatterns = [
    path("register/", views.register_view, name="register"),
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('home/', views.home, name="home"),
    path('list/', views.list_view, name="list_view"),
    path('listing/<uuid:id>/', views.listing_view, name="listing"),
    path('edit/<uuid:id>/', views.edit_view, name="edit_view"),
    path('like/<uuid:id>/', views.like_listing_view, name="like"),
    path('sendmail/<uuid:id>/', views.send_test_email, name="sendmail"),
    # path('api/listing/', ListingCreateAPIView.as_view(), name="api_listing_create"),
    # path('api/listing/<uuid:id>/update/', ListingUpdateAPIView.as_view(), name='listing-update'),
    # path('api/listing/<uuid:id>/', ListingRetrieveUpdateDestroyAPIView.as_view(), name='api-listing-detail'),
    path("testdrive/<uuid:id>/", views.testdrive_booking, name="testdrive"),
    path("my-testdrives/", views.my_test_drive_requests, name="my_test_drives"),


]


