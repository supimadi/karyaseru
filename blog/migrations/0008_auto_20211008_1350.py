# Generated by Django 3.2.7 on 2021-10-08 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210929_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(null=True, upload_to='', verbose_name='Icon Kategory'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='ig_account',
            field=models.CharField(help_text='Isi dengan link instagram penulis.', max_length=100, verbose_name='Link Akun Instagram'),
        ),
    ]
