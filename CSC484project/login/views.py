
from django.views.generic import TemplateView
from django.shortcuts import render

def login(request):
    return render(request, 'loginView.html')

class HomePageView(TemplateView):
    template_name = 'homeView.html' 

