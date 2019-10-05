import pickle


def p2():
    """
    将pickle 的数据 转化为Python 数据
    """
    p_b = b"\x80\x02}q\x00(X\b\x00\x00\x00childrenq\x01]q\x02X\x06\x00\x00\x00statusq\x03X\a\x00\x00\x00SUCCESSq\x04X\x06\x00\x00\x00resultq\x05NX\t\x00\x00\x00tracebackq\x06Nu."
    return pickle.loads(p_b)
    # pickle 只能在Python 中使用, 跨语言不行
    # pickle 可以转化Python 中所有的数据类型和类, 函数
    # pickle 的结果是 b 模式