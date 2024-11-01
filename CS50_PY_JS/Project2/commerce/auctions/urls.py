from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createListing", views.createListing, name="createListing"),
    path("currentListing<str:id>", views.currentListing, name="currentListing"),
    path("updateWatchlist<int:id>", views.updateWatchlist, name="updateWatchlist"), 
    path("placeBid", views.placeBid, name="placeBid")
    
]
