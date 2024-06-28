from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("searchResult", views.search, name="search"),
    path("createNewPage",views.createNewPage, name= "createNewPage" ),
    path("addPage",views.addPage, name= "addPage" ),
    path("updatePage",views.updatePage,name="updatePage"),
    path("randomPage",views.randomPage,name="randomPage"),
    path("editPage/<str:title>",views.editPage, name= "editPage" ),
    path("<str:title>", views.title, name="title"),
     
]
