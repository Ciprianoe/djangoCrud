from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError




# Create your views here.
def signup(request):
    active = 'signup'
    title = 'Signup'
    if request.method  == 'GET':
     return render(request,'signup/signup.html',{
        'form': UserCreationForm,
        'active':active,
        'title':title,        
        })
    else:
       if request.POST['password1'] == request.POST['password2']:
          try:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')
          except IntegrityError:
             return render(request,'signup/signup.html',{
        'form': UserCreationForm,
        'active':active,
        'title':title,
        'error':'Username already exist'        
        })
    return render(request,'signup/signup.html',{
        'form': UserCreationForm,
        'active':active,
        'title':title,
        'error':'Password do no Match'        
        })


def home(request):
    active = 'home'
    title = 'Home Page'
    return render(request, 'index.html',{"title":title, "active":active})

def tasks(request):
    active = 'tasks'
    title='Task Page'
    return render(request, 'tasks/task.html',{"title":title, "active":active})