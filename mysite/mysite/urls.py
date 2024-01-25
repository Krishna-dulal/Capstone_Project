from django.contrib import admin
from django.urls import include, path
from NisulkaGyan.views import HomeView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("NisulkaGyan/", include("NisulkaGyan.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),  
]
