from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _# Create your models here.
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth import get_user_model
USER = get_user_model()

class Topic (models.Model):
    TOPIC_NAME_REGEX = RegexValidator(r'[a-zA-Z0-9-_\.~%]+$', 'Invalide topic name')
    name = models.CharField(_('Topic Name'),max_length=255, validators=[TOPIC_NAME_REGEX])
    users = models.ManyToManyField(to=USER, related_name="subscribtion")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name