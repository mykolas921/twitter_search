from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import twitter.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("search/", twitter.views.TwitterSearchView.as_view(), name="search")
]
