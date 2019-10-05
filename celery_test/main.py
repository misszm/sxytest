import time

from tasks import qwe, test_task, ert, app
from other_tasks import asd, zxc
from test import p2


def main():
    for i in range(10):
        # test_task.delay('qqweqweqweqweqewqweqweqwe')
        # qwe.delay(1)
        ret = ert.delay(i)  # broker先接受, celery异步执行和主进程分开
        print(ret)
        # time.sleep(1)
        print(ret)
        print(ret.id)
        print(ret.status)  # "SUCCESS" 执行成功 "PENDING" 未执行完
        # print(ret.get(timeout=1))  # 如果worker没有启动, 这里会报错
        print(ret.get())  # 如果worker没有启动, 这里会卡
        print(2314234234)


if __name__ == '__main__':
    # 最好先启动worker 再启动项目, 后启动worker 也行
    """
    celery -A tasks worker --loglevel=info ： 前台启动命令
    celery multi start w1 -A tasks -l info ： 后台启动命令
    celery multi restart w2 -A tasks -l info ： 后台重启命令
    celery multi stop w3 -A tasks -l info ： 后台停止命令
    可以启动多个worker,(异步进行, 会更快) 后台可以重定向到文件
    celery -A tasks beat -l info  前台启动定时任务  # 暂未有后台命令, 定时任务不会多个重复执行
    """
    main()
    print(p2())  # 获取Redis中保存的任务执行结果, celery 自动更新
