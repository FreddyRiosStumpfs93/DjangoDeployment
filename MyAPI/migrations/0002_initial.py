# Generated by Django 4.1.6 on 2023-04-08 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MyAPI', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='user_creation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_creation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='position',
            name='user_updated',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chapter',
            name='user_creation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_creation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chapter',
            name='user_updated',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
