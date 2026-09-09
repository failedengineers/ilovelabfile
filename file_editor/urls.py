from django.contrib import admin
from django.urls import path
from file_editor import views

urlpatterns = [   path('',views.file,name="file_editor")


       # main page
    ]