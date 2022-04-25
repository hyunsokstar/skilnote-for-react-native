# Generated by Django 3.2.7 on 2021-09-24 21:50

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
            name='MyTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sub1', models.TextField(blank=True)),
                ('sub2', models.TextField(blank=True)),
                ('sub3', models.TextField(blank=True)),
                ('sub4', models.TextField(blank=True)),
                ('sub5', models.TextField(blank=True)),
                ('sub6', models.TextField(blank=True)),
                ('sub7', models.TextField(blank=True)),
                ('sub8', models.TextField(blank=True)),
                ('sub9', models.TextField(blank=True)),
                ('sub10', models.TextField(blank=True)),
                ('sub11', models.TextField(blank=True)),
                ('sub12', models.TextField(blank=True)),
                ('sub13', models.TextField(blank=True)),
                ('sub14', models.TextField(blank=True)),
                ('sub1_memo', models.TextField(blank=True)),
                ('sub2_memo', models.TextField(blank=True)),
                ('sub3_memo', models.TextField(blank=True)),
                ('sub4_memo', models.TextField(blank=True)),
                ('sub5_memo', models.TextField(blank=True)),
                ('sub6_memo', models.TextField(blank=True)),
                ('sub7_memo', models.TextField(blank=True)),
                ('sub8_memo', models.TextField(blank=True)),
                ('sub9_memo', models.TextField(blank=True)),
                ('sub10_memo', models.TextField(blank=True)),
                ('sub11_memo', models.TextField(blank=True)),
                ('sub12_memo', models.TextField(blank=True)),
                ('sub13_memo', models.TextField(blank=True)),
                ('sub14_memo', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MySite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=50)),
                ('site_url', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
