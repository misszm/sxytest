import subprocess
import time
import datetime
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler
# from django_apscheduler.jobstores import DjangoJobStore

# from cron.models import TaskLog
from django_apscheduler.jobstores import DjangoJobStore

from log_cf import logger

scheduler = BackgroundScheduler({
# scheduler = BlockingScheduler({
    # 'apscheduler.jobstores.default': {
    #     'type': 'sqlalchemy',
    #     'url': 'mysql+pymysql://root:Mysqlsxy@zm520@192.168.179.133/crontask?charset=utf8'
    # },
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


def my_listener(event):
    if event.exception:
        task_error_deal(event)
    else:
        logger.info(event.job_id + " success")


scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
scheduler.start()


def create_week_report():
    logger.warning("this is first inner func")
    print("************this is first inner func")


def http_job():
    pass


def cmd_job():
    pass


def inner_job(cmd_data):
    inner_func = {"周报": create_week_report, "日报": create_week_report}
    func_name = cmd_data["func_name"]
    func_params = cmd_data.get("func_params")
    func_params = () if not func_params else [i.strip() for i in func_params.split(",")]
    inner_func[func_name](*func_params)


def my_job(job_type, cmd_params, job_name):
    s_time = time.time()
    # tl_obj = TaskLog.objects.create(start_date=datetime.datetime.fromtimestamp(s_time),
    #                        status="执行中", task_name=job_name,
    #                        )
    type_dict = {"inner": inner_job, "http": http_job, "cmd": cmd_job}
    type_dict[job_type](cmd_params)
    sch_job_obj = scheduler.get_job(job_name)
    # tl_obj.next_run_time = sch_job_obj
    # tl_obj.task = sch_job_obj.
    # log_dict["end_date"] = datetime.datetime.now()
    # log_dict["duration"] = time.time() - s_time


def exec_shell(shell_cmd):
    """执行shell命令函数"""
    sub = subprocess.Popen(shell_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = sub.communicate()
    ret = sub.returncode
    if ret == 0:
        return ret, stdout.decode('utf-8').split('\n')
    else:
        return ret, stdout.decode('utf-8').replace('\n', '')


def my_job1(name):
    qweqweqweqw
    a, b = exec_shell("cdqq /; ls")
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


def task_error_deal(event):
    print("312423423423423423423")
    logger.error("job_id: " + event.job_id + "\n" + event.traceback + "\n" + str(type(event.exception)) + " " + str(
        event.exception))
    print("***************************************************")


if __name__ == '__main__':
    job_id = 'job_interval'
    # scheduler.remove_job(job_id)
    scheduler.add_job(my_job1, args=['job_interval', ],
                      id=job_id, trigger='interval', seconds=30, replace_existing=True, )
    scheduler.start()
    # scheduler.add_job(my_job, args=['job_interval', ],
    #                   id="1231231231", next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=5),
    #                   replace_existing=True, )
    time.sleep(100)
