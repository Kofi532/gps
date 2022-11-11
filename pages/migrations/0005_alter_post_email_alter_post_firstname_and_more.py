# Generated by Django 4.0.8 on 2022-11-09 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_post_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.EmailField(default='..', max_length=254),
        ),
        migrations.AlterField(
            model_name='post',
            name='firstname',
            field=models.CharField(default='..', max_length=25),
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(default='..', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='surname',
            field=models.CharField(default='..', max_length=25),
        ),
    ]
