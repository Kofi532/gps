# Generated by Django 4.0.8 on 2022-11-10 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approve', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Approve',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='green', max_length=6),
        ),
    ]
