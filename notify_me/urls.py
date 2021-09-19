"""notify_me URL Configuration

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
from django.urls import path, re_path, include
from fcm_django.api.rest_framework import FCMDeviceViewSet, FCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
router = DefaultRouter()
router.register(r'devices', FCMDeviceViewSet)

urlpatterns = [
    path("", include("home.urls",namespace="home")),
    path('topics/', include("topics.urls",namespace="topics"),name="topics"),

    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='FCM django web demo')),
    path('fcm/', include(router.urls)),

]

