"""
URL configuration for myblog_project project.

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
from django.urls import path, include
from myblog import views as myblog_views 
from myblog.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('myblog/', include('myblog.urls')),

    # user urls
    path('home/', myblog_views.home, name='home'), 
    path('new/', myblog_views.new_post, name='new_post'),
    path('edit/<int:pk>/', myblog_views.edit_post, name='edit_post'),
    path('post/<int:pk>/delete/', myblog_views.delete_post, name='delete_post')
]

