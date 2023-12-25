"""CRUDPROJ URL Configuration

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
from . import views
urlpatterns = [
    
    path('', views.login, name='login'),
    path('logincheck/', views.logincheck, name='verify_login'),
    path('home/', views.index, name='home'),
    
    path('register/', views.register, name='register'),
    path('registeruser/', views.registeruser, name='registeruser'),
    path('deleteuser/<int:id>', views.deleteme, name='delete'),
    path('edituser/<int:id>', views.editme, name='edit'),
    path('searchdata/', views.searchdata, name='search'),
    path('logout/', views.logout, name='logout'),
    
    
]