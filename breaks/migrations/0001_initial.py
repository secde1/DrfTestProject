# Generated by Django 4.2.6 on 2023-10-25 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='organisations', to=settings.AUTH_USER_MODEL, verbose_name='Директор')),
                ('employees', models.ManyToManyField(null=True, related_name='organisations_employees', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудники')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организация',
                'ordering': ('name',),
            },
        ),
    ]
