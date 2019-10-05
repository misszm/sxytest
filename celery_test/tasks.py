import time
from datetime import timedelta

from celery import Celery, platforms
from celery.schedules import crontab

from constans import *

# 修改celery app 后要重启worker
# 添加celery 任务后要重启worker
broker = "redis://:{}@{}:{}/{}".format(REDIS_PW, REDIS_IP, REDIS_PORT, REDIS_DB_BROKER)
backend = "redis://:{}@{}:{}/{}".format(REDIS_PW, REDIS_IP, REDIS_PORT, REDIS_DB_BACKEND)
# 包含所有的文件中的celery 任务
include = ['tasks', 'other_tasks']
app = Celery('a', broker=broker, backend=backend, include=include)
platforms.C_FORCE_ROOT = True  # 代码设置celery 可以root用户启动
# app.conf.update(
#      CELERY_ACCEPT_CONTENT = ['json'],
#      CELERY_TASK_SERIALIZER = 'json',
#      CELERY_RESULT_SERIALIZER = 'json',
# )

# 设置worker 执行结果报错时间 秒
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)
app.conf.CELERY_TIMEZONE = 'Asia/Shanghai'


@app.task
def test_task(n):
    time.sleep(10)
    print(n)
    return 123


@app.task
def test_task1(s):
    time.sleep(1)
    print(s)
    return 666


@app.task
def qwe(s):
    print(s)


@app.task
def ert(s):
    print(s)


app.conf.CELERYBEAT_SCHEDULE = {
    'every 10 seconds': {
        'task': 'tasks.ert',
        'schedule': timedelta(seconds=10),  # 可以用timedelta对象
        # 'schedule': 10,  # 也支持直接用数字表示秒数
        'args': (1,),
    },
    'every 2 minutes': {
        'task': 'tasks.qwe',
        'schedule': crontab(minute='*/2'),  # 定时任务
        'args': ('abc',),
    },
}
