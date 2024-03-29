from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import TemplateView 
from . import views
from NisulkaGyan.views import HomeView


urlpatterns = [
    # path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("", HomeView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),

]