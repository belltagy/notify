from django.urls import path, re_path, include

from rest_framework.documentation import include_docs_urls
from .views import CreateSubscriptionView
urlpatterns = [
    path("subscribe/<int:pk>/",CreateSubscriptionView.as_view(), name="subscribe" ),
]