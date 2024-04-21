from django.shortcuts import render,redirect
from todo_app.models  import *
from django.contrib import messages
from datetime import date

def index(request):
    return render(request,"index.html")

def register(request):
    return render(request,"register.html")

def registerAction(request):
    name=request.POST['name']
    age = request.POST['age']
    username=request.POST['username']
    password = request.POST['password']
    data = Register_tb(Name=name,Age=age,Username=username,Password=password)
    data.save()
    messages.add_message(request,messages.INFO,"Registration Succesfull")
    return redirect('index')
    
def login(request):
    return render(request,"login.html")

def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    data = Register_tb.objects.filter(Username=username,Password=password)
    if len(data)>0:
        request.session['userid']=data[0].id
        messages.add_message(request,messages.INFO,"Login Succesfull")
        user_id = request.session['userid']
        todo_data = Todo_list.objects.filter(User_id=user_id)
        return render(request,"userhome.html",{'data':todo_data})
    else:
        messages.add_message(request,messages.INFO,"Login Failed")
        return redirect('login')

def userhome(request):
    user_id = request.session['userid']
    todo_data = Todo_list.objects.filter(User_id=user_id)
    return render(request,"userhome.html",{'data':todo_data})

def add_project(request):
    return render(request,"add_project.html")

def addprojectAction(request):
    user_id = request.session['userid']
    title = request.POST['project_title']
    description = request.POST['description']
    current_date = date.today()
    todo_data = Todo_list(Project_title=title,Description=description,Date=current_date,Status="pending",User_id_id=user_id)
    todo_data.save()
    return redirect('userhome')


def viewproject(request,id):
    data = Todo_list.objects.filter(id=id)
    task_data = Todo_task.objects.filter(List_id=id,Task_status="pending")
    task_data1 = Todo_task.objects.filter(List_id=id,Task_status="completed")
    completed_count = task_data1.count()
    total_task = task_data.count() + completed_count
    return render(request,"viewproject.html",{'datas':data,'task':task_data,'tasks':task_data1,'completed_count':completed_count,'total_task':total_task})

def addtaskAction(request):
    addtask = request.POST['addtask']
    list_id = request.POST['list_id']
    data = Todo_task(Task=addtask,Task_status="pending",List_id_id=list_id)
    data.save()
    pending_task = Todo_task.objects.filter(List_id=list_id,Task_status="pending").exists()
    if pending_task:
        Todo_list.objects.filter(id=list_id).update(Status="pending")
    else:
        Todo_list.objects.filter(id=list_id).update(Status="completed")
    return redirect('viewproject',id=list_id)

def completedtask(request):
    task = request.POST.getlist('task')
    list_id = request.POST['list_id']
    for i in task:
        task_data = Todo_task.objects.filter(id=i).update(Task_status="completed")
    pending_task = Todo_task.objects.filter(List_id=list_id,Task_status="pending").exists()
    if pending_task:
        Todo_list.objects.filter(id=list_id).update(Status="pending")
    else:
        Todo_list.objects.filter(id=list_id).update(Status="completed")
    return redirect('viewproject',id=list_id)

def edit_project_title(request):
    list_id = request.POST['list_id']
    edit_project_title = request.POST['edit_project_title']
    data = Todo_list.objects.filter(id=list_id).update(Project_title=edit_project_title)
    return redirect('viewproject',id=list_id)

def deleteproject(request,id):
    delete_data = Todo_list.objects.filter(id=id).delete()
    return redirect('userhome')

def deletetask(request,id):
    data = Todo_task.objects.filter(id=id)
    for i in data:
        list_id = i.List_id_id
        print(list_id)
    delete_task = Todo_task.objects.filter(id=id).delete()
    return redirect('viewproject',id=list_id)

def logout(request):
    request.session.flush()
    return redirect('index')
    



# Create your views here.
