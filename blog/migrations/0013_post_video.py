# Generated by Django 3.2.7 on 2021-10-13 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20211008_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.URLField(null=True, verbose_name='Video Link'),
        ),
    ]
