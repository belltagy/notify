from django.contrib import admin

# Register your models here.
from .models import Topic

class TopicAdmin(admin.ModelAdmin):
    pass
admin.site.register(Topic,TopicAdmin)