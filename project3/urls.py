"""
URL configuration for project3 project.

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
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('date/<int:year>-<int:month>-<int:day>/', views.date),
    re_path(r'^title/(?P<title>[-\w\s]+)/$', views.show_title, name='show_title'),
    path('map/', views.maps),
    path('filter/custom/', views.filter_custom),
    path('redirect/from/', views.redirect_from, name='redirect_from'),
    path('redirect/to/', views.redirect_to, name='redirect_to'),
    path('redirect/error/<int:code>/<str:text>/',
         views.redirect_error, name='redirect_error'),
    path('main/', views.main),
    path('home/', views.home),
    path('products/', views.products),
    path('bootstrap/', views.bootstrap)
]


