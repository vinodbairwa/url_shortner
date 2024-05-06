"""
URL configuration for url_shortner project.

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
from url_shortner import views


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('create/',views.create),
    path('update/',views.verify),
    path('signin/',views.login),
    path('forpwd/',views.forgot_password),
    path('chpwd/',views.change_password),
    path('urlshort/',views.url_shortner),
    path('longurl/',views.get_long_url),
    path('allurl/',views.get_all_url),
    
]

