# Generated by Django 3.2.18 on 2023-04-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230328_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='description',
        ),
        migrations.AddField(
            model_name='tag',
            name='descriptions',
            field=models.CharField(default='now empty :(', max_length=100),
        ),
    ]
