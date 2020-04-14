import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View


from cron.apsch_cf import scheduler, my_job
from cron.models import CronTask


def resp(msg=None, code=1001, data=None):
    return JsonResponse({"msg": msg, "code": code, "data": data})


class TaskView(View):
    def get(self, request):
        scheduler.get_jobs()
        pass

    def post(self, request):
        params = json.loads(request.body) if request.body else {}
        name = params.get("name")
        ct_q = CronTask.objects.filter(name=name)
        if ct_q.exists():
            return resp("任务名称已存在")
        cron_data = dict()

        start_date = params.get("start_date")
        end_date = params.get("end_date")
        # interval = params.get("interval")
        # scheduler.add_job(my_job, args=['job_interval', ],
        #                   id=name, trigger='interval', seconds=interval, replace_existing=True, )
        month = params.get("month")  # 1-12
        day = params.get("day")  # 1-31
        day_of_week = params.get("day_of_week")  # 0-6
        day_of_week = day_of_week if day_of_week == "日" else int(day_of_week) - 1
        hour = params.get("hour")
        minute = params.get("minute")
        second = params.get("second")
        job_type = params.get("job_type")
        if job_type not in ("inner", "http", "command"):
            return resp("任务类型错误")
        cmd = params.get("cmd")
        cron_data["id"] = name
        cron_data["start_date"] = start_date
        cron_data["end_date"] = end_date
        cron_data["month"] = month
        cron_data["day"] = day
        cron_data["day_of_week"] = day_of_week
        cron_data["hour"] = hour
        cron_data["minute"] = minute
        cron_data["j"] = second
        a = scheduler.get_job(name)
        scheduler.remove_all_jobs()
        # scheduler.add_job(my_job, "cron", start_time=start_time, end_time=end_time,
        #                   month=month, day=day, day_of_week=day_of_week, hour=hour,
        #                   minute=minute, second=second)
        sch_job = scheduler.add_job(my_job, "cron", args=(job_type, cmd, name), **cron_data)
        # print(sch_job)
        # cron_data["job_type"] = job_type
        # cron_data["cmd"] = cmd
        # CronTask.objects.create(**cron_data)
        return resp(code=1000)

    def put(self, request):
        job_id = "name"
        scheduler.modify_job(job_id, minutes=5)
        scheduler.pause_job(job_id)  # 暂停任务  下次运行时间留空
        scheduler.resume_job(job_id)  # 恢复任务
        scheduler.pause()  # 暂停未执行的任务
        scheduler.resume()
        # 立即执行一次
        return resp(code=100)

    def delete(self, request):
        job_id = "name"
        scheduler.remove_job(job_id)
        return resp(code=100)
