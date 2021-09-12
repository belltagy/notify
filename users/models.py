from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator, MinLengthValidator,RegexValidator
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this

class User(AbstractUser):
    pass