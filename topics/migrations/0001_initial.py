# Generated by Django 3.1 on 2021-09-19 09:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('[a-zA-Z0-9-_\\.~%]+$', 'Invalide topic name')], verbose_name='Topic Name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('users', models.ManyToManyField(related_name='subscribtion', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]