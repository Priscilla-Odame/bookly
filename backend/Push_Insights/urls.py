"""Push_Insights URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('surveys/', include('surveys.urls')),
    path('projects/', include('projectapp.urls')),
    path('api/report/', include('report.urls')),
    path('api/fruits/', include('fruits.urls')),
    path('celery-progress/', include('celery_progress.urls'), name="celery_progress"),
    path('docs/', include_docs_urls(title='Push Insights Api')),
]
