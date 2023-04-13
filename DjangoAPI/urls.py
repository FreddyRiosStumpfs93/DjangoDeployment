"""DjangoAPI URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from homepage.views import IndexView
from login.views import LoginFormView, LoginFormView2
from DjangoAPI import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Segundo ejemplo
    # path('apicalling/', include('apicalling.urls'))

    # probando cambiar el home
    # path('home/', include('MyAPI.urls')),
    path('myapi/', include('MyAPI.urls')),
    path('', IndexView.as_view(), name='index'),
    path('login/', include('login.urls')),
    path('user/', include('user.urls')),

]

## SOLO VÁLIDO PARA DESARROLLO
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)