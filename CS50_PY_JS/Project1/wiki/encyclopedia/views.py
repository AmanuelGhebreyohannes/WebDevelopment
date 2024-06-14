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
            for entry in util.list_entries:
                if(title in entry):
                    new_entries.append(entry)
            return render(request, "encyclopedia/index.html", {
                "entries": new_entries,
                "searchForm":forms.SearchForm
            })
            

        return render(request, "encyclopedia/title.html", {
            "title": title,
            "description":description,
            "page_available":page_available,
            "searchForm":forms.SearchForm
        })


