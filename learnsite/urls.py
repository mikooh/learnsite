"""learnsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views  # Here '.' means 'this directory'... because views is saved in the same directory. we import it here

urlpatterns = [
    path('', views.home, name='home'),  # the empty '' represent that, if user doesn't give any information, take them to the place mentioned after the comma. here we want them to go to a function on the views page. hence views.function. use comma at the end before the next path.
    path('countss/', views.count, name='count'),
    path('about/', views.about, name='about')
]
# Basically 'admin/' represents the url. so shridharlifeschool.com/admin should work only because admin has been given here. all the sites urls are listed here.
