from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import dataForm

def home(request):
    posts = data.objects.all()
    return render(request, 'index.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def create(request):  
    if request.method == "POST":  
        form = dataForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('about')  
            except:  
                pass  
    else:  
        form = dataForm()  
    return render(request,'about.html',{'form':form})  