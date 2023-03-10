"""category URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from myApp import views

urlpatterns = [
    path('', views.assignment, name='assignment'),
    path('query1/', views.query1, name='query1'),
    path('query2/', views.query2, name='query2'),
    path('query3/', views.query3, name='query3'),
    path('query4/', views.query4, name='query4'),
    path('create/', views.create, name='create'),
    path('insert/', views.insert, name='insert'),
    path('drop/', views.drop, name='drop'),
    path('check/', views.check, name='check'),
]