from django.urls import path

from . import views

app_name = 'encyclopedia'
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>/", views.title, name="title"),
    path("/search/", views.search, name="search"),
    path("/search/<str:name>", views.searchByname, name="searchByname"),
    path("/create/", views.create, name="create"),
    path("/create/add_entry", views.add_entry, name="add_entry"),
    path("/randomly/", views.randomly, name="randomly"),
    path("/edit/", views.edit, name="edit"),
    path("/edit/editpage", views.editpage, name="editpage"),
    path("/edit/editpage/update_entry", views.update_entry, name="update_entry")
]
