# Generated by Django 3.0.2 on 2020-02-01 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=88)),
                ('apellido_paterno', models.CharField(max_length=99)),
                ('apellido_materno', models.CharField(max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=88)),
                ('apellido_paterno', models.CharField(max_length=99)),
                ('apellido_materno', models.CharField(max_length=99)),
                ('email', models.EmailField(max_length=100)),
                ('fecha_registro', models.DateTimeField(verbose_name='date published')),
                ('edad', models.IntegerField(default=18)),
                ('direccion', models.TextField(default='Lima - Perú')),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=88)),
                ('precio', models.IntegerField(default=1)),
                ('marca', models.CharField(max_length=99)),
                ('stock', models.IntegerField(default=100)),
            ],
        ),
    ]