from django.shortcuts import render
from django.http import HttpResponse
from . models import Formation, Experience
# Create your views here.

def index(request):
   Formations = Formation.objects.order_by('start_date')
   Experiences = Experience.objects.order_by('start_date')
   return  render(request, 'website/index.html',{'Formations': Formations, 'Experiences':Experiences})
 
def contact(request):
    return render(request, 'website/contact.html')

def about(request):
   return render (request, 'website/about.html')