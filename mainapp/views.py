from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login ,logout, authenticate
from django.db import IntegrityError
from .forms import CreateTaskForm
from .models import Task





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
            #login(request, user)
            return redirect('signin')
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

def logoutsesion(request):
   logout(request)
   print('session borrada')
   return redirect(signup)

def signin(request):
   active = 'signin'
   title = 'Signin'
   if request.method  == 'GET':
     return render(request, 'signin/signin.html',{'active':active, 'title':title, 'form':AuthenticationForm()})
   else:
      user = authenticate( request, username=request.POST['username'], password=request.POST['password'])
   if user is None:
         return render(request, 'signin/signin.html',{'active':active, 'title':title, 'error':'User or password is wrong!!', 'form':AuthenticationForm()})
   else:
      login(request, user)
      return redirect('home')

def home(request):
    active = 'home'
    title = 'Home Page'
    return render(request, 'index.html',{"title":title, "active":active})

def tasks(request):
    active = 'tasks'
    title='Task Page'
    task = Task.objects.all()
    return render(request, 'tasks/task.html',{"title":title, "active":active, 'task':task})

def createtask(request):
   active = 'tasks'
   title = 'Create Task'
   if request.method == 'GET':
      print(request.GET)
      return render(request, 'tasks/create_task.html', {"title":title, 'active':active, 'form': CreateTaskForm()} )
   else:
      task=CreateTaskForm(request.POST)
      new_task = task.save(commit=False)
      new_task.user = request.user
      new_task.save()
      return redirect('tasks')
      