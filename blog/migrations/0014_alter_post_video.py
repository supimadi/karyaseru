# Generated by Django 3.2.7 on 2021-10-13 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.URLField(blank=True, help_text='Masukan link video jika ada, untuk disematkan di artikel.', null=True, verbose_name='Link Video'),
        ),
    ]