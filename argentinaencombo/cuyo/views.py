from django.shortcuts import render
from .models import Project

# Create your views here.
def cuyo (request):
    projects = Project.objects.all()
    return render (request,"cuyo/cuyo.html", {'projects': projects})