from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogs



# Create your views here.




def home(request):
    context = {'posts' : Blogs.objects.all(),'title' :' Home'}
    return render(request,"blogApp/blogHome.html",context)

def about(request):
    return render(request,"blogApp/blogAbout.html")