# Generated by Django 3.2.18 on 2023-04-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230405_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='descriptions',
            field=models.CharField(default='now empty', max_length=100),
        ),
    ]
