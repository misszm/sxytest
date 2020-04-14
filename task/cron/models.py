from django.db import models


class CronTask(models.Model):
    id = models.AutoField(verbose_name='ID', primary_key=True)
    user_id = models.IntegerField(verbose_name="用户id", null=False)
    name = models.CharField(verbose_name='任务名称', max_length=256, null=True)
    type = models.CharField(verbose_name='任务类型', max_length=128, null=False)  # inner, http, cmd, 对应哪个任务调用方法
    cmd = models.CharField(verbose_name="可执行命令", max_length=2048, null=False)  # 看类型,
    start_date = models.DateTimeField(verbose_name="开始时间", null=True)
    end_date = models.DateTimeField(verbose_name="结束时间", null=True)  # 周期任务截止时间
    interval = models.PositiveIntegerField(verbose_name="间隔时间", null=True)  # 任务执行间隔时间 s 前段如: 0月0天0小时3分10秒
    month = models.CharField(verbose_name="哪几月", max_length=128, null=True)  # 在哪几个月运行  1-12
    day = models.CharField(verbose_name="每月哪几天", max_length=128, null=True)  # 在每月哪几天运行 1-31
    day_of_week = models.CharField(verbose_name="每星期哪几天", max_length=128, null=True)  # 在星期几运行 0-6(周一到周日)
    hour = models.CharField(verbose_name="哪几小时", max_length=128, null=True)  # 0-23
    minute = models.CharField(verbose_name="哪几分钟", max_length=128, null=True)  # 0-59
    second = models.CharField(verbose_name="哪几秒", max_length=128, null=True)  # 0-59
    delete = models.NullBooleanField(verbose_name="是否删除", default=False)  # 默认任务未删除


class TaskLog(models.Model):
    id = models.AutoField(verbose_name='ID', primary_key=True)
    task_name = models.CharField(verbose_name='任务名称', max_length=256, null=True)
    start_date = models.DateTimeField(verbose_name="开始时间", null=False)  # 本次开始时间
    end_date = models.DateTimeField(verbose_name="结束时间", null=True)  # 本次截止时间
    duration = models.CharField(verbose_name="执行一次耗时", max_length=128, null=True)  # 任务一次执行用时
    next_run_time = models.DateTimeField(verbose_name="下次执行时间", null=True)  # 周期任务下次执行时间
    status = models.CharField(verbose_name="任务状态", max_length=10, null=False)  # 执行中, 已结束, 暂停, 失败
    exception = models.CharField(verbose_name="执行出错类型", max_length=64, null=True)  # 定时任务执行出错的类型
    traceback = models.TextField(verbose_name="执行出错信息", null=True)  # 定时任务执行出错的具体信息
    result_msg = models.TextField(verbose_name="返回信息", null=True)  # 一次任务执行后的返回信息
