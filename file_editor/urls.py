from django.contrib import admin
from django.urls import path
from file_editor import views

urlpatterns = [   path('',views.file,name="file_editor"),
                # file_editor/urls.py
            path('change-enrollment-number-ggsipu-pdf/', views.guide_ggsipu, name='guide_ggsipu'),
            path('edit-name-roll-number-dtu-lab-file-pdf/', views.guide_dtu, name='guide_dtu'),
            path('replace-text-college-pdf-practical-file/', views.guide_replace_text, name='guide_replace_text'),
            path('ai/',views.ai,name='ai'),
            # urls.py
            path('copied-friend-lab-file-name-change/', views.guide_friend_copy, name='guide_friend_copy'),
            path('workshop-file-pdf-editor/', views.guide_workshop_file, name='guide_workshop_file'),


       # main page
    ]