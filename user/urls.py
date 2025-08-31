from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name="login_view"),
    path('register/', views.Registerview.as_view(), name="Register"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.Profileview.as_view(), name="profile"),
]