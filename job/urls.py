"""job URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path, include
from django.contrib import admin
from home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('lei/', views.lei, name='lei'),
    path('parceiros/', views.parceiros, name='parceiros'),
    path('sobre/', views.sobre, name='sobre'),
    path('dicas/', views.dicas, name='dicas'),
    path('gerador/', views.gerador, name='gerador'),
    path('op/', views.op, name='op'),
    path('admin/', admin.site.urls),
    path('jovem/', include('jovem.urls')),
    path('empresa/', include('empresa.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
