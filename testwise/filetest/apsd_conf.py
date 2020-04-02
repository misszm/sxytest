import os
import subprocess
import time
import datetime
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler
from django_apscheduler.jobstores import DjangoJobStore

from filetest.log.log_cf import logger

scheduler = BackgroundScheduler({
# scheduler = BlockingScheduler({
#     'apscheduler.jobstores.default': {
#         'type': 'sqlalchemy',
#         'url': 'mysql+pymysql://root:Mysqlsxy@zm520@localhost/crontask?charset=utf8'
#         # 'url': 'sqlite:///jobs.sqlite'
#     },
    'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '20'
    },
    'apscheduler.executors.processpool': {
        'type': 'processpool',
        'max_workers': '5'
    },
    'apscheduler.job_defaults.coalesce': 'True',  # True错过的任务只会执行一次 False全部执行
    'apscheduler.job_defaults.max_instances': '1',  # 同一个任务同一时间最多执行的次数
    'apscheduler.job_defaults.misfire_grace_time': 1,  # 如果不写默认1s 只会执行预定在过去一秒内的任务
})
scheduler.add_jobstore(DjangoJobStore(), "default")


class Task:

    def _exec_shell(shell_cmd):
        """执行shell命令函数"""
        sub = subprocess.Popen(shell_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = sub.communicate()
        ret = sub.returncode
        if ret == 0:
            return ret, stdout.decode('utf-8').split('\n')
        else:
            return ret, stdout.decode('utf-8').replace('\n', '')


def my_job1(name):
    a, b = Task._exec_shell("cdqq /; ls")
    time.sleep(3)
    print(name)
    logger.error(str(datetime.datetime.now()) + str(a) + str(b))
    for ret in [scheduler.get_job(job_id)]:
        logger.error(str(ret.next_run_time))
    if a == 0:
        return "success"


def task1(x):
    print(x)
    print(x)
    print(x)
    print(x)


def my_listener(event):
    if event.exception:
        print("312423423423423423423")
        logger.error("job_id: " + event.job_id + "\n" + event.traceback + "\n" + str(type(event.exception)) + " " + str(event.exception))
        print("***************************************************")
    else:
        logger.info(event.job_id + " success")
scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
scheduler.start()
if __name__ == '__main__':
    job_id = 'job_interval'
    # scheduler.remove_job(job_id)
    scheduler.add_job(my_job1, args=['job_interval', ],
                      id=job_id, trigger='interval', seconds=1, replace_existing=True, )
    # scheduler.add_job(my_job, args=['job_interval', ],
    #                   id="1231231231", next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=5),
    #                   replace_existing=True, )
    time.sleep(100)
