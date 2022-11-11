# Generated by Django 4.1.3 on 2022-11-08 19:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('cover', models.ImageField(upload_to='images/')),
                ('surname', models.CharField(default='DEFAULT VALUE', max_length=25)),
                ('firstname', models.CharField(default='DEFAULT VALUE', max_length=25)),
                ('level', models.CharField(default='DEFAULT VALUE', max_length=25)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
