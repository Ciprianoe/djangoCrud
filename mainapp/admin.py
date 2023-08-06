from django.contrib import admin
from .models import Task

#para ver el campo que no se vizualiza en el panel 
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)


# Register your models here.
admin.site.register(Task, TaskAdmin)