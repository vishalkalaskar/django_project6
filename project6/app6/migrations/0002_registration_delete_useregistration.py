# Generated by Django 4.0.1 on 2022-01-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app6', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='useregistration',
        ),
    ]