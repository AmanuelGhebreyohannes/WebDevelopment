from django.shortcuts import render

from . import util
from . import forms

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "searchForm":forms.SearchForm
    })

def title(request,title):
    description = util.get_entry(title)
    page_available = True
    if(description == None):
        page_available = False
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "description":description,
        "page_available":page_available,
        "searchForm":forms.SearchForm
    })



def search(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = util.get_entry(title)
        page_available = True
        if(description == None):
            page_available = False
        new_entries = []
        if(page_available == False):
            for entry in util.list_entries():
                if(title in entry):
                    new_entries.append(entry)
                    page_available=True
            if(page_available):        
                return render(request, "encyclopedia/index.html", {
                    "entries": new_entries,
                    "searchForm":forms.SearchForm
                })
            else:
                return render(request, "encyclopedia/index.html", {
                    "entries": util.list_entries(),
                    "searchForm":forms.SearchForm
                })
            

        return render(request, "encyclopedia/title.html", {
            "title": title,
            "description":description,
            "page_available":page_available,
            "searchForm":forms.SearchForm
        })
    
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "searchForm":forms.SearchForm
    })


def createNewPage(request):
    return render(request, "encyclopedia/createNewPage.html",{
        "createNewPageForm":forms.NewPageForm,
        "error":""
    })

def addPage(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('content')
        if(title in util.list_entries()):
           return render(request, "encyclopedia/createNewPage.html",{
            "createNewPageForm":forms.NewPageForm,
            "error":"Title already Exists!!!"
            })
        else:
            with open("entries/"+title+".md", 'w') as file:
                file.write(f'# {title} \n {description}')
            
            return render(request, "encyclopedia/title.html", {
                "title": title,
                "description":util.get_entry(title),
                "page_available":True,
                "searchForm":forms.SearchForm
                })




    return render(request, "encyclopedia/createNewPage.html",{
        "createNewPageForm":forms.NewPageForm,
        "error":"Unable to save Page! Please try again!"
    })