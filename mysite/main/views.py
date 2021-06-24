from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    contact_info = Contact.objects.all()
    return render(request, 'main/index.html', context={'contact_info': contact_info})
