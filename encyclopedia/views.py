from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import default_storage
from markdown2 import Markdown
from django import forms

from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content")


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

def newpage(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title,content)
            return HttpResponseRedirect("/")
        else:
            return render(request, "encyclopedia/newPage.html", {
                "form": form
            })
        
    return render(request, "encyclopedia/newPage.html", {
        "form": NewPageForm()
    })
  