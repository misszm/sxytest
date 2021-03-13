import os
import time
import turtle
import random
from matplotlib import pyplot as plt
from matplotlib import image as img
from PIL import Image, EpsImagePlugin


# def petal_backup(m, t):
#     t.getscreen().tracer(30, 0)
#     for i in range(m):
#         a = 200 - 400 * random.random()
#         b = 10 - 20 * random.random()
#
#         t.up()
#
#         t.forward(b)
#         t.left(90)
#         t.forward(a)
#         t.down()
#         t.color("lightcoral")
#         t.circle(1)
#         t.up()
#         t.backward(a)
#         t.right(90)
#         t.backward(b)
#     for i in range(m):
#         radius = random.randint(100, 150)
#         angle = random.random() * 360
#         t.left(angle)
#         t.up()
#         t.forward(radius)
#         t.down()
#         t.dot(2, 'lightcoral')
#         t.home()
#     # aa = 100
#     # for a, b, m in ((150, 200, 250), (100, 150, 60), (5, 98, 20)):
#     #     a += aa
#     #     b += aa
#     #     for i in range(4):
#     #         for i in range(int(m/4)):
#     #             radius = random.randint(a, b)
#     #             angle = random.random() * 360
#     #             t.up()
#     #             t.left(angle)
#     #             t.forward(radius)
#     #             t.down()
#     #             t.color("lightcoral")
#     #             t.circle(1)
#     #             t.up()
#     #             t.home()
#     #             t.left(90)
#     #             t.backward(200)
#     #             t.down()


def tree(bl, t):
    # time.sleep(0.001)
    if bl > 3:
        if 8 <= bl <= 12:
            if random.randint(0, 2) == 0:
                t.color("snow")
            else:
                t.color("lightcoral")
            t.pensize(bl / 3)
        elif bl < 8:
            if random.randint(0, 1) == 0:
                t.color("snow")
            else:
                t.color("lightcoral")
            t.pensize(bl / 2)
        else:
            t.color("sienna")
            t.pensize(bl / 10)
        t.forward(bl)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        tree(bl - 10 * b, t)
        t.left(40 * a)
        tree(bl - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(bl)
        t.down()


def petal(m, t):
    t.pensize(3)
    t.getscreen().tracer(30, 0)
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        a = 1.8 * a
        b = 1.8 * b
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color("lightcoral")
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


def insert_py_pic(w, t, py_pic_path="py_no_qing.gif"):
    w.addshape(py_pic_path)  # 新增形状
    t.shape(py_pic_path)  # 替换小乌龟
    t.goto(380, -270)
    st_id = t.stamp()
    return st_id


def gen_phone_num():
    phone_num_path = "phone_num.gif"
    if os.path.exists(phone_num_path):
        return
    a_list = [
        [0, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9,
         0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0],
        [0, 9, 5, 1, 1, 2, 9, 3, 9, 1, 0, 9, 2, 1, 1, 2, 9, 3, 1, 1, 1, 9, 5, 1, 1, 1, 9, 5, 9, 1, 1, 9, 5, 9, 1, 0, 9,
         2, 1, 1, 1, 9, 5, 1, 2, 0, 9, 1, 1, 1, 0, 9, 0],
        [3, 9, 2, 1, 0, 9, 2, 2, 9, 1, 0, 9, 2, 1, 0, 1, 9, 2, 1, 2, 0, 9, 2, 1, 2, 0, 9, 2, 9, 9, 9, 9, 2, 9, 1, 0, 9,
         2, 1, 2, 0, 9, 2, 0, 1, 2, 9, 2, 1, 2, 9, 3, 0],
        [4, 9, 1, 2, 9, 1, 1, 0, 9, 1, 0, 9, 2, 2, 3, 9, 1, 0, 1, 0, 0, 9, 1, 1, 0, 0, 9, 1, 1, 2, 0, 9, 1, 9, 1, 0, 9,
         2, 1, 0, 0, 9, 1, 3, 2, 9, 1, 0, 2, 9, 1, 0, 0],
        [5, 9, 3, 2, 0, 9, 1, 0, 9, 1, 0, 9, 2, 0, 9, 2, 1, 0, 3, 0, 0, 9, 3, 3, 0, 0, 9, 3, 3, 0, 0, 9, 3, 9, 1, 0, 9,
         2, 3, 0, 0, 9, 3, 1, 9, 0, 0, 3, 0, 2, 9, 1, 0],
        [4, 9, 1, 1, 0, 2, 9, 0, 9, 1, 0, 9, 2, 9, 0, 2, 1, 0, 1, 0, 1, 9, 1, 1, 0, 1, 9, 1, 1, 0, 1, 9, 1, 9, 1, 0, 9,
         2, 1, 0, 1, 9, 1, 9, 2, 1, 1, 0, 1, 2, 3, 9, 0],
        [2, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 0, 1, 0, 1, 9, 0, 1, 0, 1, 9, 0, 1, 0, 1, 9, 0, 9, 9, 9, 9,
         2, 1, 0, 1, 9, 0, 9, 9, 9, 9, 1, 9, 9, 9, 9, 0]]
    phone_num_png_path = "phone_num.png"
    plt.matshow(a_list, cmap="bone", alpha=0.3, origin="upper")
    plt.axis("off")
    plt.savefig(phone_num_png_path, bbox_inches="tight", pad_inches=0,
                orientation="landscape", transparent=True)  # 横向, 透明
    # plt.savefig(phone_num_png_path, bbox_inches="tight", pad_inches=0, orientation="landscape")  # 横向, 透明
    plt.close()
    plt.figure(figsize=(10, 1.5))
    pic = img.imread(phone_num_png_path)
    plt.imshow(pic)
    plt.axis("off")
    # plt.savefig(phone_num_png_path, bbox_inches="tight", pad_inches=0, orientation="landscape")  # 横向
    plt.savefig(phone_num_png_path, bbox_inches="tight", pad_inches=0, orientation="landscape",
                transparent=True)  # 透明
    plt.close()
    os.rename(phone_num_png_path, phone_num_path)


def main():
    gen_phone_num()
    drawing()


def drawing():
    t = turtle.Turtle()
    w = turtle.Screen()
    t.hideturtle()
    t.getscreen().tracer(100, 0)
    w.setup(1200, 700)  # 设置窗口大小, 屏幕大小, 可以最大化
    # w.setworldcoordinates(0, 0, 1200, 700)
    # w.screensize(bg="wheat", canvwidth=800, canvheight=700)  # 设置画布大小
    # w.screensize(bg="wheat")
    w.screensize(bg="#ffdac8")  # 粉
    # w.screensize(bg="#a3e2c5")  # 艾青
    w.title("whose eyes lock me")

    zm(t)
    zm(t, False)

    # t.color("black")
    # t_write(*(t, 370, -280, ".py", ("Arial", 16, "normal")))

    py_no_stamp_id = insert_py_pic(w, t)

    t.goto(0, 0)
    t.left(180)
    t.up()
    t.backward(200)
    t.down()
    t.color("sienna")

    tree(70, t)  # 正好
    petal(200, t)
    insert_phone_pic(w, t, py_no_stamp_id)
    write_name(t)
    # save_jpg(w)

    w.exitonclick()


def zm(t, flag=True):
    t.color("#ffdac8")
    # t.color("#ffe6d9")
    t.pensize(4)
    t.up()
    if flag:
        t.goto(-380, 0)
        t.down()
        t.forward(60)
        t.right(125)
        t.forward(110)
        t.left(125)
        t.forward(62)
    else:
        t.goto(310, -90)
        t.down()
        t.left(90)
        t.forward(92)
        t.right(160)
        t.forward(95)
        t.left(140)
        t.forward(95)
        t.right(160)
        t.forward(92)
    t.up()
    t.pensize(1)


def insert_phone_pic(w, t, stamp_id, pic_path="phone_num.gif"):
    t.getscreen().tracer(1, 0)
    w.addshape(pic_path)  # 新增形状
    t.shape(pic_path)  # 替换小乌龟
    time.sleep(ts)
    t.showturtle()
    time.sleep(ts)
    t.up()
    t.goto(0, 0)
    st_id_1 = t.stamp()
    # t.hideturtle()
    time.sleep(ts)
    t.goto(0, 200)
    t.showturtle()
    ss = 0.5
    time.sleep(ts-ss)
    t.clearstamp(st_id_1)
    t.hideturtle()
    time.sleep(ts-ss)
    st_id_2 = t.stamp()
    t.goto(0, -200)
    t.showturtle()
    time.sleep(ts-ss)
    t.clearstamp(st_id_2)
    t.hideturtle()
    time.sleep(ts-ss)
    w.screensize(bg="#a3e2c5")  # 艾青
    py_qing_stamp_id = insert_py_pic(w, t, py_pic_path="py_qing.gif")
    t.clearstamp(stamp_id)
    t.goto(0, 0)
    time.sleep(ts-ss)
    t.clearstamp(py_qing_stamp_id)
    w.screensize(bg="#ffdac8")  # 粉


def save_jpg(w):
    w.getcanvas().postscript(file='./result.eps')
    EpsImagePlugin.gs_windows_binary = r'E:\gs9.53.3\bin\gswin64c.exe'
    pic = Image.open("./result.eps")
    pic.save("./result.jpg")


def t_write(t, x, y, v, font=("仿宋", 30, "normal")):
    font = list(font)
    t.goto(x, y)
    if v in "XY":
        font[1] = 34
    t.write(v, font=font)


def write_name(t):
    t.getscreen().tracer(1, 0)
    t.pensize(3)
    t.up()
    t.color("red")
    a, b = -100, 60
    for x, y, v in ((-280, -210, "喜"), (-280, -245, "阳"), (-300, -210, "X"), (-300, -245, "Y")):
        t_write(t, x + a, y + b, v)
        time.sleep(ts - 0.65)
    t.goto(-231 + a, -205 + b)
    t.down()
    t.circle(43)
    t.up()
    t.pensize(1)


if __name__ == '__main__':
    ts = 1
    main()
