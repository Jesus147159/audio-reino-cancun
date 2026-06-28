from django.urls import path

from .views import api_create_lead, api_site_content, home


urlpatterns = [
    path("", home, name="home"),
    path("api/site/", api_site_content, name="api_site_content"),
    path("api/leads/", api_create_lead, name="api_create_lead"),
]
