from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request,title):
    description = util.get_entry(title)
    page_available = True
    if(description == None):
        page_available = False
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "description":description,
        "page_available":page_available
    })

