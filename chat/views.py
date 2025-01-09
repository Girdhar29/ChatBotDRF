
from django.http import HttpResponse
from django.template import loader
from .models import Student


def home(request):
     myusers = Student.objects.all().values()
     template = loader.get_template('index.html')
     context = {
    'myusers': myusers,
     }
     return HttpResponse(template.render(context, request))



 
