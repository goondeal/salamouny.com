from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    contact_info = Contact.objects.all()
    projects = Project.objects.all()
    return render(request, 'main/index.html', context={'projects': projects, 'contact_info': contact_info, })
