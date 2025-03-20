"""
URL configuration for pomodoroTimerProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import front_page
from .views import home_page
from .views import edit_task
from .views import delete_task
from .views import search_task

urlpatterns = [
    path("", front_page, name="front_page"),
    path("home/", home_page, name="home_page"),
    path("task/", search_task, name="search_task"),
    path(
        "edit_task/<int:task_id>/<int:page_number>/",
        edit_task,
        name="edit_task",
    ),
    path(
        "delete_task/<int:task_id>/<int:page_number>/",
        delete_task,
        name="delete_task",
    ),

]
