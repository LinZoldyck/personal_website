from django.shortcuts import render
from django.http import HttpResponse
from . models import Formation
# Create your views here.

def index(request):
   Formations = Formation.objects.order_by('status')
   return  render(request, 'website/index.html',{'Formations': Formations})
 
def contact(request):
    return render(request, 'website/contact.html')