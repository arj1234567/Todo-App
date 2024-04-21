from django.db import models

class Register_tb(models.Model):
    Name = models.CharField(max_length=20)
    Age = models.CharField(max_length=20)
    Username=models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    
class Todo_list(models.Model):
    Project_title = models.CharField(max_length=20)
    Description = models.CharField(max_length=20)
    Date = models.CharField(max_length=20)
    Status = models.CharField(max_length=20)
    User_id = models.ForeignKey(Register_tb,on_delete=models.CASCADE)
    
class Todo_task(models.Model):
    Task = models.CharField(max_length=20)
    Task_status = models.CharField(max_length=20)
    List_id = models.ForeignKey(Todo_list,on_delete=models.CASCADE)

# Create your models here.
