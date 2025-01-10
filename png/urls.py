"""
URL configuration for networkapp project.

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.urls import path
from .views import *

urlpatterns = [
path('',index, name="index"),
path('register',register, name="register"),
path('event',event, name="event"),
path('news',news,name="news"),
    path('login',login_view,name="login"),
    path('admin_page',landing, name="landing"),
    path('partners',partners1,name='partners')

]



