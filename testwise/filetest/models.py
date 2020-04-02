# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# class ICSLTest(models.Model):
#     id = models.AutoField(verbose_name='ID', primary_key=True, db_column='id')
#     file_report = models.FileField(verbose_name='报告文件', null=True, upload_to=".", max_length=256)


class CronTask(models.Model):
    id = models.AutoField(verbose_name='ID', primary_key=True)
    name = models.CharField(verbose_name='任务名称', max_length=128)
    status = models.CharField(verbose_name="任务状态", max_length=10)  # 执行中, 未开始, 已结束, 暂停, 失败
    cmd = models.CharField(verbose_name="可执行命令", max_length=2048)  # 直接在服务器上执行的命令
    start_time = models.DateTimeField(verbose_name="任务开始时间")  # 适用只执行一次
    interval = models.PositiveIntegerField(verbose_name="间隔时间")  # 任务执行间隔时间 s 前段如: 0月0天0小时3分10秒
