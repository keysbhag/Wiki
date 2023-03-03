from django.shortcuts import render

from django.core.files.storage import default_storage

from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def result(request,title):
    markdowner = Markdown()
    if (util.get_entry(title)):
        return render(request, "encyclopedia/result.html", {
            "info": markdowner.convert(util.get_entry(title))
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })
    
def search(request):
    _, filenames = default_storage.listdir("entries")
    query = request.GET.get("q", "")
    markdowner = Markdown()

    for filename in filenames:
        if (query+".md").lower() == filename.lower():
            return render(request, "encyclopedia/result.html", {
                "info": markdowner.convert(util.get_entry(query))
            })
        
    return render(request,"encyclopedia/search.html", {
        "searches": util.search_entries(query)
    })
  