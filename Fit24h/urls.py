"""Fit24h URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic.base import TemplateView
from backend.views import getRoutineList
from backend.views import postRoutineList
from backend.views import getAllPosts
from backend.views import newPost
from backend.views import getUser


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', TemplateView.as_view(template_name='index.html')),
    path(r'api/crt', getRoutineList),
    path(r'api/crtp', postRoutineList),
    path(r'api/psts', getAllPosts),
    path(r'api/npst', newPost),
    path(r'api/usr', getUser)
]
