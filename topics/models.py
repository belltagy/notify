from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _# Create your models here.
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# topic name validators
TOPIC_NAME_REGEX = RegexValidator(r'[a-zA-Z0-9-_\.~%]+$', 'Invalide topic name')

def topic_name_validator(value):
    import re
    if re.fullmatch(r'^[a-zA-Z0-9-_\.~%]+$', value):
        return True
    else :
        from django.core.exceptions import ValidationError
        return ValidationError(message="Invalide topic name")

class Topic (models.Model):
    name = models.CharField(_('Topic Name'),max_length=255, validators=[TOPIC_NAME_REGEX]) #check unique required
    users = models.ManyToManyField(to=User, related_name="subscribtion", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(verbose_name=_("Admin"), to=User, related_name= "my_topics", on_delete=models.SET_NULL,
                                null=True, blank=True)
    # slug field to save unique
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)