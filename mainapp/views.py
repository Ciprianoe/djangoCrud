from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login ,logout, authenticate
from django.db import IntegrityError
from .forms import CreateTaskForm
from .models import Task
from django.utils import timezone
from random import random
from django.contrib.auth.decorators import login_required





# Create your views here.

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return '#%02x%02x%02x' % (r, g, b)


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

@login_required
def logouts(request):
   logout(request)
   return redirect(signin)

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

@login_required
def home(request):
    active = 'home'
    title = 'Home Page'
    task = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'index.html',{"title":title, "active":active, 'task':task})

@login_required
def tasks(request):
    active = 'tasks'
    title='Task Page'
    task = Task.objects.filter(user=request.user, datecompleted__isnull=True).order_by('-important','-id')
    return render(request, 'tasks/task.html',{"title":title, "active":active, 'task':task})

@login_required
def createtask(request):
   active = 'tasks'
   title = 'Create Task'
   if request.method == 'GET':
      print(request.GET)
      return render(request, 'tasks/create_task.html', {"title":title, 'active':active, 'form': CreateTaskForm()} )
   else:
      try:
         task=CreateTaskForm(request.POST)
         new_task = task.save(commit=False)
         new_task.user = request.user
         new_task.save()
         return redirect('tasks')
      except ValueError:
         return render(request, 'tasks/create_task.html', {"title":title, 'active':active, 'form': CreateTaskForm(),'error':'error in data'} )

@login_required      
def taskeditdetails(request,id):
    active = 'tasks'
    title='Task edit details'
    task = Task.objects.filter(id=id)
    return render(request, 'tasks/tasks_edit_details.html',{'active':active,'title':title, 'task':task, 'form':CreateTaskForm()})      

@login_required
def edittask(request,id):
    active = 'tasks'
    title='Task edit'
    if request.method == 'GET':
         task = get_object_or_404(Task,id=id, user=request.user)
         form = CreateTaskForm(instance=task)  
         return render(request, 'tasks/edit_task.html',{'active':active,'title':title, 'task':task, 'form':form})
    else:
         try:
            print(request.POST)
            task = get_object_or_404(Task,id=id, user=request.user)
            form=CreateTaskForm(request.POST,instance=task)
            form.save()
            return redirect('tasks')
         except ValueError:
             return render(request, 'tasks/edit_task.html',{'active':active,'title':title, 'task':task, 'form':form,'error':'Error updating task'})

@login_required         
def taskdone(request,id):
   task = get_object_or_404(Task,id=id, user=request.user)
   if task:
      task.datecompleted = timezone.now()
      task.save()
      return redirect('tasks')         

@login_required            
def taskdelete(request,id):
   task = get_object_or_404(Task, id=id, user=request.user)
   if task:
      task.delete()
      return redirect('tasks')
   


