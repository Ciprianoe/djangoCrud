from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logouts, name='logout'),
    path('home/', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('createtask/', views.createtask, name='createtask'),
    path('taskeditdetails/<int:id>', views.taskeditdetails, name='taskeditdetails'),
    path('taskedit/<int:id>', views.edittask, name='taskedit'),
    path('taskdone/<int:id>', views.taskdone, name='taskdone'),
    path('taskdelete/<int:id>', views.taskdelete, name='taskdelete'),
]