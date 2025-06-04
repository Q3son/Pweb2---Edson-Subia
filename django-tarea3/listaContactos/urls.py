"""
URL configuration for listaContactos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from inicio.views import myHomeView, anotherView
from personas.views import inicio
from django.views.generic import TemplateView


urlpatterns = [
    path('', myHomeView, name='inicio'),
    path('another/', anotherView, name='otra-pagina'),
    path('pro/', TemplateView.as_view(template_name='experimental/home_pro.html')),
    path('admin/', admin.site.urls),
]