"""
URL configuration for perutourism project.

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
from django.conf import settings
from django.conf.urls.static import static
from destinos import views as destinos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', destinos_views.home, name='home'),
    path('destinos/', include('destinos.urls')),
    path('accounts/register/', destinos_views.register_view, name='register'),
    path('accounts/logout/', destinos_views.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)