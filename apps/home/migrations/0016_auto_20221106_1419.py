# Generated by Django 3.2.6 on 2022-11-06 14:19

import apps.home.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20221104_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='btn_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='post',
            name='document',
            field=models.FileField(default='', upload_to='', verbose_name='Документ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='music',
            field=models.FileField(default='', upload_to='', verbose_name='Музыкальный Трек'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='photo_1',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото 1'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_2',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото 2'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_3',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото 3'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_4',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото 4'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_5',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото 5'),
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.CharField(max_length=300, null=True, validators=[apps.home.validators.post_ref_validator], verbose_name='Ссылка'),
        ),
        migrations.AddField(
            model_name='post',
            name='url_text',
            field=models.CharField(max_length=300, null=True, verbose_name='Текст внутри ссылки'),
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(default='', upload_to='', verbose_name='Видео Запись'),
            preserve_default=False,
        ),
    ]