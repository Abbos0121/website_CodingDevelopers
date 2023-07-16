from django.contrib import admin
from django.urls import path, include
from .views import newApp
from django.conf.urls.static import static
from django.conf import settings
from new_app.views import search_view

urlpatterns = [
    path('', newApp, name="new-app"),
    path('search/', search_view, name="search"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)