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
    t.getscreen().tracer(1, 0)
    w.setup(1200, 700)  # 设置窗口大小, 屏幕大小, 可以最大化
    # w.screensize(bg="wheat", canvwidth=800, canvheight=700)  # 设置画布大小
    w.screensize(bg="wheat")

    zm(t)

    t.goto(0, 0)
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color("sienna")

    # tree(60, t)
    # petal(100, t)
    write_name(t)
    insert_pic(w, t)
    # save_jpg(w)

    w.exitonclick()


def zm(t):
    t.color("black")
    t.pensize(5)
    t.up()
    t.goto(-500, 200)
    t.down()
    t.forward(400)
    t.right(130)
    t.forward(600)
    t.left(130)
    t.forward(400)
    t.up()
    pass


def insert_pic(w, t):
    # import os
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # bg_path = os.path.join(current_dir, "bg.PNG")
    # w.bgpic(bg_path)
    # pic_path = os.path.join(current_dir, "add.gif")
    pic_path = "phonenumber_size1111.gif"
    w.addshape(pic_path)  # 新增形状
    t.shape(pic_path)  # 替换小乌龟
    t.goto(0, 0)


def save_jpg(w):
    w.getcanvas().postscript(file='./result.eps')
    EpsImagePlugin.gs_windows_binary = r'E:\gs9.53.3\bin\gswin64c.exe'
    pic = Image.open("./result.eps")
    pic.save("./result.jpg")


def write_name(t):
    def t_write(x, y, v, font=("仿宋", 30, "normal")):
        t.goto(x, y)
        t.write(v, font=font)
    t.up()
    t.color("black")
    for x, y, v in ((280, 280, "X"), (280, 247, "Y"), (300, 280, "喜"), (300, 245, "阳")):
        t_write(x, y, v)
    t_write(*(-300, 280, ".py", ("Arial", 16, "normal")))
    t.goto(349, 285)
    t.down()
    # t.up()
    t.circle(41)
    t.up()


if __name__ == '__main__':
    main()


# 改变乌龟图标, 保存, 在加载, 在改变乌龟图标, 在保存
