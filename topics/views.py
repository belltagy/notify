from django.shortcuts import render
from django.views.generic import ListView
from .models import Topic
# Create your views here.

class TopicsView(ListView):
    template_name = "topics/topics_list.html"
    queryset = Topic.objects.all()
    