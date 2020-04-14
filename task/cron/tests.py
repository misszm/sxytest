import datetime
import time

from django.test import TestCase

# Create your tests here.


def inner_job(cmd_data):
    inner_func = {"create_week_report": create_week_report}
    func_name = cmd_data["func_name"]
    func_params = cmd_data.get("func_params")
    func_params = () if not func_params else [i.strip() for i in func_params.split(",")]
    inner_func[func_name](*func_params)


def my_job(job_type, cmd_params):
    type_dict = {"inner": inner_job, "http": http_job, "cmd": cmd_job}
    type_dict[job_type](cmd_params)


def create_week_report():
    print("this is first inner func")


def http_job():
    pass


def cmd_job():
    pass


if __name__ == '__main__':
    # my_job("inner", {"func_name": "create_week_report"})
    a = datetime.datetime.now()
    print(a)
    aa = time.mktime(a.timetuple())
    print(aa)
    b = time.time()
    print(b)
    c = datetime.datetime.fromtimestamp(b)
    print(c)
    ffff = type(123)
    a = 123
    print(ffff)