# Generated by Django 2.0.5 on 2020-03-25 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CronTask',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('name', models.CharField(max_length=128, verbose_name='任务名称')),
                ('type', models.CharField(max_length=128, verbose_name='任务类型')),
                ('cmd', models.CharField(max_length=2048, verbose_name='可执行命令')),
                ('start_time', models.DateTimeField(null=True, verbose_name='开始时间')),
                ('end_time', models.DateTimeField(null=True, verbose_name='结束时间')),
                ('month', models.CharField(max_length=128, null=True, verbose_name='哪几月')),
                ('day', models.CharField(max_length=128, null=True, verbose_name='每月哪几天')),
                ('day_of_week', models.CharField(max_length=128, null=True, verbose_name='每星期哪几天')),
                ('hour', models.CharField(max_length=128, null=True, verbose_name='哪几小时')),
                ('minute', models.CharField(max_length=128, null=True, verbose_name='哪几分钟')),
                ('second', models.CharField(max_length=128, null=True, verbose_name='哪几秒')),
                ('delete', models.NullBooleanField(default=False, verbose_name='是否删除')),
            ],
        ),
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(null=True, verbose_name='结束时间')),
                ('run_time', models.CharField(max_length=128, null=True, verbose_name='执行一次耗时')),
                ('next_time', models.DateTimeField(null=True, verbose_name='下次执行时间')),
                ('status', models.CharField(max_length=10, verbose_name='任务状态')),
                ('exception', models.CharField(max_length=64, null=True, verbose_name='执行出错类型')),
                ('traceback', models.TextField(null=True, verbose_name='执行出错信息')),
                ('result_msg', models.TextField(null=True, verbose_name='返回信息')),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cron.CronTask')),
            ],
        ),
    ]
