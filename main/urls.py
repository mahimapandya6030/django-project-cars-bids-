from django.contrib import admin
from django.urls import path
from . import views
from uuid import UUID
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
    
]
