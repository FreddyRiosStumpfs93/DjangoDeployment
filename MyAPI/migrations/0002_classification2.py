# Generated by Django 4.1.6 on 2023-04-17 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('description', models.CharField(max_length=50, verbose_name='Descripción')),
                ('material', models.CharField(choices=[('Plastico', 'Plástico'), ('Vidrio', 'Vidrio'), ('Ceramica', 'Cerámica')], max_length=25, verbose_name='Material')),
                ('classify', models.CharField(max_length=25)),
                ('user_creation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_creation', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Clasificación',
                'verbose_name_plural': 'Clasificaciones',
                'ordering': ['classify'],
            },
        ),
    ]