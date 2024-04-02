from django.template import loader
from django.http import HttpResponse

def login(request):
    template = loader.get_template('loginView.html')
    return HttpResponse(template.render())