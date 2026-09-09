from django.contrib import admin
from django.urls import path
from file_editor import views

urlpatterns = [   path('',views.file,name="file_editor"),
                # file_editor/urls.py
            path('change-enrollment-number-ggsipu-pdf/', views.guide_ggsipu, name='guide_ggsipu'),
            path('edit-name-roll-number-dtu-lab-file-pdf/', views.guide_dtu, name='guide_dtu'),
            path('replace-text-college-pdf-practical-file/', views.guide_replace_text, name='guide_replace_text'),


       # main page
    ]