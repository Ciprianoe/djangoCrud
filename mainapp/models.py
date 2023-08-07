from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
""" modelo para las task """
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)   #este campo no se vizualiza en el panel admi
    datecompleted = models.DateTimeField(null=True, blank=True)  #con el blank true puedes set en el admin y salta el req
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title +' By: '+ self.user.username