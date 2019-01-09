"""DjangoWithIntellijApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#from DjangoWithIntellijApp import views #import mymodule is the python file.
import DjangoWithIntellijApp #böylede oluyor name lookup'a dahil ediyorum bu paketi klasörü gibi
from DjangoWithIntellijApp.views import year_archive #o zaman böylede olur o zaman aslında import method dedik

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/<int:year>/', year_archive), #year_archive metodu çağrılacak gibi tasarlamışlar.
]
