# Generated by Django 4.0.8 on 2022-11-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approve', '0003_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Comments',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='Approve',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='None', max_length=6),
        ),
    ]
