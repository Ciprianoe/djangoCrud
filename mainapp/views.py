from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





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
            return HttpResponse('User created successfully')
          except:
             return HttpResponse('Username already exits')
    return HttpResponse('password do not match')


def home(request):
    active = 'home'
    title = 'Home Page'
    return render(request, 'index.html',{"title":title, "active":active})

def tasks(request):
    active = 'tasks'
    title='Task Page'
    return render(request, 'tasks/task.html',{"title":title, "active":active})