from django.db import models
from django.db.models import fields
from ..models import Topic
from rest_framework import serializers

class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = "__all__"
