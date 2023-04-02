# Generated by Django 3.2.18 on 2023-03-27 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230320_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='at now hollow knight', max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(blank=True, help_text='in format yyyy-mm-dd', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='O', max_length=6),
        ),
    ]
