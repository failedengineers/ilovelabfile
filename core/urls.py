from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from file_editor.sitemaps import StaticViewSitemap

handler404 = "file_editor.views.custom_404"

sitemaps = {'static': StaticViewSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('', include('file_editor.urls')),
]