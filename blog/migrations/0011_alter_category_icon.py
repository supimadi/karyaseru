# Generated by Django 3.2.7 on 2021-10-08 08:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_category_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.FileField(null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['jpeg', 'jpg', 'png', 'svg', 'gif', 'bmp'])], verbose_name='Icon Kategory'),
        ),
    ]
