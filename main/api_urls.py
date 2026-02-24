# from django.urls import path, include
# from .api_views import listing_api, single_listing_api, Testdriveapiview, TestDriveListCreateView, TestDriveRUDView
# from .views import Listingviewset
# from rest_framework.routers import DefaultRouter


# listing_mark_sold = Listingviewset.as_view({
#     'post': 'mark_sold'
# })

# # router = DefaultRouter()
# # router.register('listings', Listingviewset, basename='listings')


# urlpatterns = [
#     path('listing/', listing_api),
#     path('listing/<uuid:id>/', single_listing_api),
#     path("testdrive/", Testdriveapiview.as_view(), name="testdrive"),
#     path("testdrives_lc/", TestDriveListCreateView.as_view()),
#     path("testdrives/<int:pk>/", TestDriveRUDView.as_view()),
    
#     path('listing/<uuid:pk>/mark_sold/', listing_mark_sold, name='listing-mark-sold'),

#         # path('', include(router.urls)),
    

# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Listingviewset
from .api_views import (
    listing_api,
    single_listing_api,
    Testdriveapiview,
    TestDriveListCreateView,
    TestDriveRUDView
)
router = DefaultRouter()
router.register('listings', Listingviewset, basename='listings')

urlpatterns = [
    # Your old APIViews 
    path('listing-old/', listing_api),
    path('listing-old/<uuid:id>/', single_listing_api),

    path("testdrive/", Testdriveapiview.as_view(), name="testdrive"),
    path("testdrives_lc/", TestDriveListCreateView.as_view()),
    path("testdrives/<int:pk>/", TestDriveRUDView.as_view()),

    # ViewSet Routes
    path('', include(router.urls)),
]




