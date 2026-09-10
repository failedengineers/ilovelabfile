from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        return ['file_editor', 'guide_ggsipu', 'guide_dtu', 'guide_replace_text']

    def location(self, item):
        return reverse(item)