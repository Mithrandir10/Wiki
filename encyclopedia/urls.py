from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/<str:a>", views.entry, name="entry"),
    path("npage",views.new_page,name="npg"),
    path("edit/<str:x>",views.edit_page,name="edit")
]
