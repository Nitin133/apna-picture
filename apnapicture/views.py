from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import redirect

from myapp.models import *

def show_home_page(request):
    cats=category .objects.all()
    images=image.objects.all()
    data={'images':images,'cats':cats}





    return render (request,"home.html",data)

def show_category_page(request,cid):
    
    cats=category .objects.all()
    cat=category.objects.get(pk=cid)
   





    images=image.objects.filter(cat=cat)
    data={'images':images,'cats':cats}





    return render (request,"home.html",data)
def home(request):
    return redirect('/home')
    