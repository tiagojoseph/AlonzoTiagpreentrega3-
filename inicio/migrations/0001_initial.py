# Generated by Django 5.1.2 on 2024-10-24 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propiedades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metros_cuadrados', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=20)),
                ('precio', models.CharField(max_length=20)),
            ],
        ),
    ]