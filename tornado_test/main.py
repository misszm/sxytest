# -*- coding: utf-8 -*-
import asyncio
import tornado.ioloop
from tornado.web import Application
from tornado import httpserver
from tornado.web import url
from constant import port, ip
from view import *

from tornado.options import define, options  # 用于脚本传参

define("port", default=port, type=int, help="run server on the given port.")  # 定义服务器监听端口选项
define("ip", default=ip, type=str, help="run server on the given ip.")

settings = {
    "xsrf_cookies": True,
    "debug": True,
}


def make_app():
    return Application([
        url(r"/api/v1/fight/(20.{12,35})/", ConnFightHandler, name="current_fight_url"),
        url(r"/v/data/", DealDataHandler, name="fight_data_url"),
    ],
        # **settings
    )


def main():
    asyncio.set_event_loop(asyncio.new_event_loop())
    options.parse_command_line()
    app = make_app()
    # app.listen(port, ip)  # 是下面三行的简写, 只能是单进程

    http_server = httpserver.HTTPServer(app)
    # http_server.listen(port, ip)
    http_server.listen(options.port, options.ip)
    http_server.start()  # None或<=0即 核数  不写这行代码默认为1, 可在此使用不同端口的多进程

    logger.warning("tornado已经启动{}:{}".format(options.ip, options.port))
    # tornado.ioloop.IOLoop.current().start()
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
