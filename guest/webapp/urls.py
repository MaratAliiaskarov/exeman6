from django.urls import path

from webapp.views import index_view, create_book

urlpatterns = [
    path("", index_view),
    path("entry/add/", create_book)
]