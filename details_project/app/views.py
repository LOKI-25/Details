from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    if request.method=='POST':
        name=request.POST['name']
        skill=request.POST['skill']
        description=request.POST['description']
        obj=Details(name=name,skill=skill,description=description)
        obj.save()
    return render(request,'home.html')

def detail(request):
    obj=Details.objects.all()
    return render(request,'details.html',{'obj':obj})