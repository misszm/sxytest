# -*- coding: utf-8 -*-
import json

from tornado.websocket import WebSocketHandler

from log_cf import logger
from public import now_date

fight_conns = {
    "conn_code": dict(),
}
data_conns = {
    "conn": list()
}


class ConnFightHandler(WebSocketHandler):
    def open(self, code):  # 当一个新的WebSocket连接建立后被调用。
        """
        :param code: 作战编号
        """
        # now_day = datetime.datetime.now().strftime("%Y%m%d")
        # if
        fight_conns["conn_code"][self] = code
        logger.info("%s作战编号: %s       0" % (self.ip, code))

    def on_message(self, msg):  # 当客户端发送消息message过来时被调用，注意此方法必须被重写。
        # print("********{}:{}****".format(self.request.remote_ip, msg))
        self.close(None, "非法操作, 不允许发送消息, 连接已经断开")

    # print('*************************************')

    def on_close(self):  # 当WebSocket连接关闭后被调用。
        code = fight_conns["conn_code"].pop(self)
        logger.info("%s作战编号: %s      -1" % (self.ip, code))

    def check_origin(self, origin):
        self.ip = self.request.remote_ip
        return True  # 允许WebSocket的跨域请求  允许所有连接


class DealDataHandler(WebSocketHandler):
    flag = True
    conn = None

    def open(self):  # 当一个新的WebSocket连接建立后被调用。
        if DealDataHandler.conn: DealDataHandler.conn.close()
        DealDataHandler.conn = self
        logger.warning("%s (sxy)%s      0" % (now_date(), self.ip))

    def on_message(self, data):  # 当客户端发送消息message过来时被调用，注意此方法必须被重写。
        send_data(data, self)

    def on_close(self):  # 当WebSocket连接关闭后被调用。
        logger.warning("%s (sxy)%s    -1" % (now_date(), self.ip))
        DealDataHandler.flag = True

    def check_origin(self, origin):
        self.ip = self.request.remote_ip
        # if self.ip in ["10.20.10.91", '10.20.1.53', '192.168.130.164']:
        # if DealDataHandler.flag is True:
        # DealDataHandler.flag = False
        return True  # 允许WebSocket的跨域请求  允许所有连接


def deal_data(data, self):
    try:
        data = json.loads(data)
    except Exception as e:
        self.write_message("发送数据的格式不正确: " + str(e))
    else:
        return data


def send_data(data, self):
    data = deal_data(data, self)
    if data:
        for conn, code in fight_conns["conn_code"].items():
            if data["fight_code"] == code:  # 作战编号相同  # test
                try:
                    conn.write_message(data["fight_data"])
                except Exception as e:
                    logger.warning("给客户端: {}, 作战编号: {}, 发送作战数据失败: {}".format(conn.request.remote_ip, code, e))


if __name__ == '__main__':
    print([1, 2, 3][-1])
