# Generated by Django 3.2.6 on 2022-11-28 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20221124_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='bot',
        ),
        migrations.AddField(
            model_name='chat',
            name='bot',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.bot', verbose_name='Бот'),
        ),
    ]
