from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class HomePageview(TemplateView):
    template_name= "home.html"