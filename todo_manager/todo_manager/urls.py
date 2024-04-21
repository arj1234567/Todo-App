"""
URL configuration for todo_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('registerAction/',views.registerAction,name="registerAction"),
    path('login/',views.login,name="login"),
    path('loginAction/',views.loginAction,name="loginAction"),
    path('add_project/',views.add_project,name="add_project"),
    path('addprojectAction/',views.addprojectAction,name="addprojectAction"),
    path('viewproject/<int:id>',views.viewproject,name="viewproject"),
    path('addtaskAction/',views.addtaskAction,name="addtaskAction"),
    path('completedtask/',views.completedtask,name="completedtask"),
    path('edit_project_title/',views.edit_project_title,name="edit_project_title"),
    path('userhome/',views.userhome,name="userhome"),
    path('deleteproject/<int:id>',views.deleteproject,name="deleteproject"),
    path('deletetask/<int:id>',views.deletetask,name="deletetask"),
    path('logout/',views.logout,name="logout"),
]
