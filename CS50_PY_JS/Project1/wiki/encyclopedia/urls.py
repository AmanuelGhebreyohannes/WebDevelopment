from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("searchResult", views.search, name="search"),
    path("createNewPage",views.createNewPage, name= "createNewPage" ),
    path("<str:title>", views.title, name="title"),
     
]
