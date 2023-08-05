from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
]