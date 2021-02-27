# Generated by Django 2.0.5 on 2020-03-25 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cron', '0004_auto_20200325_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklog',
            name='task',
        ),
        migrations.AddField(
            model_name='tasklog',
            name='task_name',
            field=models.CharField(max_length=256, null=True, verbose_name='任务名称'),
        ),
        migrations.AlterField(
            model_name='crontask',
            name='name',
            field=models.CharField(max_length=256, null=True, verbose_name='任务名称'),
        ),
    ]