from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("Hello, world. You're at the NisulkaGyan index.")


# def home(request):
#     return HttpResponse("Welcome to the home page!")



class HomeView(TemplateView):
    template_name = 'home.html'

