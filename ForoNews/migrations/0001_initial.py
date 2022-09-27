# Generated by Django 4.1.1 on 2022-09-26 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='foro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(default='anonimo', max_length=200)),
                ('email', models.CharField(max_length=200, null=True)),
                ('tema', models.CharField(max_length=300)),
                ('descripcion', models.CharField(blank=True, max_length=1000)),
                ('enlace', models.CharField(max_length=100, null=True)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='discusion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discutir', models.CharField(max_length=1000)),
                ('foro', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ForoNews.foro')),
            ],
        ),
    ]