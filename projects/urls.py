from django.urls import path

from . import projects_views

urlpatterns = [
    path("", projects_views.index, name="index")
]
