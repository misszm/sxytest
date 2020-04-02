# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import subprocess

from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from filetest.apsd_conf import task1, my_job1, my_listener
from filetest.log.log_cf import logger
from testwise import settings
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")
scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
scheduler.start()
def file_test(request):
    # return HttpResponseRedirect("http://localhost:8000/" + settings.STATIC_URL + "LICENSE")
    return HttpResponseRedirect(redirect_to="http://localhost:8000/" + "LICENSE")


class Task(View):

    def _exec_shell(self, shell_cmd):
        """执行shell命令函数"""
        sub = subprocess.Popen(shell_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = sub.communicate()
        ret = sub.returncode
        if ret == 0:
            return ret, stdout.decode('utf-8').split('\n')
        else:
            return ret, stdout.decode('utf-8').replace('\n', '')

    def get(self, request):
        scheduler.remove_all_jobs()
        scheduler.add_job(my_job1, args=['job_interval', ],
                          id="sxy", trigger='interval', seconds=5, replace_existing=True, )
        # scheduler.add_job(my_job1, args=['job_interval', ],
        #                   id="1231231231", next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=500),
        #                   replace_existing=True, )

        return HttpResponse("ok")
