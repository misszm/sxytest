# -*- coding: utf-8 -*-
import base64
import datetime
import json, time

from Crypto.Cipher import AES
from log_cf import logger


class AesEbc16:
    def __init__(self):
        self.key = b"zMOmOzkt76WUW5mj"
        self.mode = AES.MODE_ECB
        self.block_size = 16

    def plaintext(self, s_text):
        b_text = str.encode(s_text)
        count = len(b_text)
        # text不是16的倍数那就补足为16的倍数
        add_count = self.block_size - (count % self.block_size)
        s_plaintext = s_text + (' ' * add_count)
        b_plaintext = str.encode(s_plaintext)
        return b_plaintext

    def encrypt(self, str_text):  # 加密
        aes_cipher = AES.new(self.key, self.mode)  # ECB模式无需向量iv
        cipher_text = aes_cipher.encrypt(self.plaintext(str_text))
        return cipher_text

    def decrypt(self, b_text):  # 解密
        aes_cipher = AES.new(self.key, self.mode)
        b_plaintext = aes_cipher.decrypt(b_text)
        return b_plaintext


def req_deal(body):  # 对app POST请求参数的处理
    try:
        l_body = json.loads(body)
        data = l_body["data"]
        data = base64.b64decode(data.encode("utf-8")).decode("utf-8")  # 解base64
        data = AesEbc16().decrypt(data)  # 解aes
        data = json.loads(data).rstrip()
    except Exception as e:
        logger.warning("解密: %s失败: %s" % (body, str(e)))
    # return {"message": "加密格式不正确", "retCode": 0},  # tuple
    else:
        return data


def resp_deal(data):  # 对app 响应参数的处理
    data = json.dumps(data)
    data = AesEbc16().encrypt(data)
    data = bytes.decode(base64.b64encode(data))  # 对base64的加密结果转str
    body = json.dumps({"data": data})
    return body


def check_input(*msg):  # 校验sql, 防注入
    characters = "*#\"$%^&~`!+=-_:;'|\\<>,/"
    for single_msg in msg:
        for i in characters:
            if i in single_msg:
                return False
    return True  # 通过


def now_date():  # 获取当前年月日时分秒的date格式  %Y-%m-%d %H:%M:%S
    return datetime.datetime.fromtimestamp(round(time.time()))


if __name__ == "__main__":
    ret = datetime.datetime.now().strftime("%Y%m%d")
    print(ret)
    print(len("11111111111122222222222222222222222"))

    pass
