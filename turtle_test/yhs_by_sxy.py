import time
import turtle
import random

from PIL import Image, EpsImagePlugin


def tree(branchLen, t):
    time.sleep(0.005)
    if branchLen > 3:
        if 8 <= branchLen <= 12:
            if random.randint(0, 2) == 0:
                t.color("snow")
            else:
                t.color("lightcoral")
            t.pensize(branchLen / 3)
        elif branchLen < 8:
            if random.randint(0, 1) == 0:
                t.color("snow")
            else:
                t.color("lightcoral")
            t.pensize(branchLen / 2)
        else:
            t.color("sienna")
            t.pensize(branchLen / 10)
        t.forward(branchLen)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        tree(branchLen - 10 * b, t)
        t.left(40 * a)
        tree(branchLen - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branchLen)
        t.down()


def petal(m, t):
    # for i in range(m):
    #     a = 200 - 400 * random.random()
    #     b = 10 - 20 * random.random()
    #     t.up()
    #     t.forward(b)
    #     t.left(90)
    #     t.forward(a)
    #     t.down()
    #     t.color("lightcoral")
    #     t.circle(1)
    #     t.up()
    #     t.backward(a)
    #     t.right(90)
    #     t.backward(b)
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
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

def main():
    t = turtle.Turtle()
    w = turtle.Screen()
    # t.hideturtle()
    t.getscreen().tracer(10, 0)
    w.setup(1200, 700)  # 设置窗口大小, 屏幕大小, 可以最大化
    # w.setworldcoordinates(0, 0, 1200, 700)
    # w.screensize(bg="wheat", canvwidth=800, canvheight=700)  # 设置画布大小
    # w.screensize(bg="wheat")
    w.screensize(bg="#ffdac8")  # 粉

    zm(t)
    zm(t, False)

    t.goto(0, 0)
    t.left(180)
    t.up()
    t.backward(200)
    t.down()
    t.color("sienna")

    # tree(80, t)  # 正好
    tree(20, t)
    petal(100, t)
    write_name(t)
    insert_pic(w, t)
    # save_jpg(w)

    w.exitonclick()


def zm(t, flag=True):
    t.color("#ffdac8")
    # t.color("#ffe6d9")
    t.pensize(20)
    t.up()
    if flag:
        t.goto(-500, 200)
        t.down()
        t.forward(400)
        t.right(130)
        t.forward(600)
        t.left(130)
        t.forward(400)
    else:
        t.goto(100, -260)
        t.down()
        t.left(90)
        t.forward(462)
        t.right(155)
        t.forward(515)
        t.left(130)
        t.forward(515)
        t.right(155)
        t.forward(462)
    t.up()
    t.pensize(1)


def insert_pic(w, t, pic_path="phonenumber_size1111.gif"):
    t.getscreen().tracer(1, 0)
    w.addshape(pic_path)  # 新增形状
    t.shape(pic_path)  # 替换小乌龟
    ts = 0.5
    t.goto(0, 0)
    st_id = t.stamp()
    time.sleep(ts)
    t.goto(0, 200)
    t.stamp()
    time.sleep(ts)
    t.clearstamp(st_id)
    time.sleep(ts)
    t.goto(0, -200)
    time.sleep(ts)
    t.clearstamps(1)
    t.hideturtle()
    time.sleep(ts)
    w.screensize(bg="#a3e2c5")  # 艾青
    t.goto(0, 0)
    time.sleep(ts)
    w.screensize(bg="#ffdac8")  # 粉


def save_jpg(w):
    w.getcanvas().postscript(file='./result.eps')
    EpsImagePlugin.gs_windows_binary = r'E:\gs9.53.3\bin\gswin64c.exe'
    pic = Image.open("./result.eps")
    pic.save("./result.jpg")


def t_write(t, x, y, v, font=["仿宋", 30, "normal"]):
    t.goto(x, y)
    if v in "XY":
        font[1] = 34
    t.write(v, font=font)


def write_name(t):
    t.pensize(3)
    t.up()
    t.color("red")
    a, b = -50, 0
    for x, y, v in ((-280, -210, "喜"), (-280, -245, "阳"), (-300, -210, "X"), (-300, -245, "Y")):
        t_write(t, x+a, y+b, v)
    t.goto(-231+a, -205+b)
    t.down()
    t.circle(43)
    t.up()
    t.color("black")
    t_write(*(t, 300, -280, ".py", ("Arial", 16, "normal")))
    t.pensize(1)


if __name__ == '__main__':
    main()

