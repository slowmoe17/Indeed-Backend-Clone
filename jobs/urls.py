from django.contrib import admin
from django.urls import URLPattern, path, include
from .views import JobList,JobDelete

urlpatterns = [

    path("list_create/", JobList.as_view()),
    path("delete/", JobDelete.as_view()),
    

]