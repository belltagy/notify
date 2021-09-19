from django.contrib import admin
from django.urls import path, re_path, include
from fcm_django.api.rest_framework import FCMDeviceViewSet, FCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from .views import TopicsView
app_name = "topics"
urlpatterns = [
    path("",TopicsView.as_view(), name="topics-list" ),
   path("api/",include("topics.api.urls")),
]