from django.shortcuts import render
from .models import Feature 

def index(request):
    
    features = Feature.objects.all()
    return render(request,'index.html',{'features' : features })


