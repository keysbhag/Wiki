from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.result, name="result"),
    path("search/", views.search, name="search"),
    path("newpage/", views.newpage, name="newpage")
]

""" Steps for solving this code:
1. make a path for each page that is needed
2. Go through the check list of each page to see what functions are need
3. Do research on how to make a form to submit to a markup and save it to the entries list
4. figure out how to convert markdown to html for viewing of entries (WE use save entry)
5. figure out search result page (we use get entry)
"""