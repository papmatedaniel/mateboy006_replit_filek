import turtle

turtle.setup(width=950, height=800, startx=10, starty=-10)
t = turtle.Turtle()
t.speed(100)


def hézalap1(x, y):
    t.begin_fill()
    t.pen(pensize=2, fillcolor="#33cc8c", pencolor="black", speed=10)
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.rt(-90)
    t.fd(142)
    t.rt(90)
    t.fd(300)
    t.rt(90)
    t.fd(142)
    t.rt(90)
    t.fd(300)
    t.end_fill()


hézalap1(-270, -106)


def Ablak1(x, y):  #ABLAKKERET
    t.begin_fill()
    t.pen(pensize=2, fillcolor="brown", pencolor="black", speed=10)
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.fd(53)
    t.rt(45)
    t.fd(13)
    t.rt(45)
    t.fd(80)
    t.rt(45)
    t.fd(13)
    t.rt(45)
    t.fd(53)
    t.rt(45)
    t.fd(13)
    t.rt(45)
    t.fd(80)
    t.rt(45)
    t.fd(13)
    t.end_fill()


Ablak1(-60, -81)


def Ablakkeret1(x, y):  #ABLAKKERET
    t.begin_fill()
    t.pen(pensize=2, fillcolor="yellow", pencolor="black", speed=10)
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.rt(45)
    t.fd(53)
    t.rt(90)
    t.fd(80)
    t.rt(90)
    t.fd(53)
    t.rt(90)
    t.fd(80)
    t.end_fill()
    t.bk(19)
    t.rt(90)
    t.fd(53)
    t.rt(90)
    t.fd(22)
    t.rt(90)
    t.fd(53)
    t.rt(-90)
    t.fd(22)
    t.rt(-90)
    t.fd(53)
    t.rt(90)
    t.fd(17)
    t.rt(90)
    t.fd(27)
    t.rt(90)
    t.fd(80)


Ablakkeret1(-60, -72)


def Ablak2(x, y):  #ABLAK
    t.begin_fill()
    t.pen(pensize=2, fillcolor="brown", pencolor="black", speed=10)
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.rt(90)
    t.fd(53)
    t.rt(45)
    t.fd(13)
    t.rt(45)
    t.fd(80)
    t.rt(45)
    t.fd(13)
    t.rt(45)
    t.fd(53)
    t.rt(45)
    t.fd(13)
    t.rt(45)
    t.fd(80)
    t.rt(45)
    t.fd(13)
    t.end_fill()


Ablak2(-179, -81)


def Ablakkeret1(x, y):  #ABLAKKERET
    t.begin_fill()
    t.pen(pensize=2, fillcolor="yellow", pencolor="black", speed=10)
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.rt(45)
    t.fd(53)
    t.rt(90)
    t.fd(80)
    t.rt(90)
    t.fd(53)
    t.rt(90)
    t.end_fill()
    t.fd(80)
    t.bk(19)
    t.rt(90)
    t.fd(53)
    t.rt(90)
    t.fd(22)
    t.rt(90)
    t.fd(53)
    t.rt(-90)
    t.fd(22)
    t.rt(-90)
    t.fd(53)
    t.rt(90)
    t.fd(17)
    t.rt(90)
    t.fd(27)
    t.rt(90)
    t.fd(80)


Ablakkeret1(-179, -72)


def háztető44(x, y):
    t.pen(pensize=2, fillcolor="#800000", pencolor="black", speed=10)
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.begin_fill()
    t.rt(90)
    t.fd(26)
    t.rt(133)
    t.fd(110)
    t.rt(47)
    t.fd(308)
    t.rt(142)
    t.fd(106)
    t.rt(-90)
    t.fd(11)
    t.rt(-90)
    t.fd(24)
    t.rt(128)
    t.fd(20)
    t.rt(90)
    t.fd(325)
    t.end_fill()
    t.penup()


háztető44(-270, 36)


def kémény(x, y):
    t.penup
    t.setposition(x, y)
    t.pendown()
    t.begin_fill()
    t.pen(pensize=3, fillcolor="#C0C0C0", pencolor="black", speed=10)
    t.rt(90)
    t.fd(36)
    t.rt(-90)
    t.fd(50)
    t.rt(-90)
    t.fd(36)
    t.end_fill()
    t.bk(36)
    t.rt(90)
    t.begin_fill()
    t.pen(pensize=3, fillcolor="#C0C0C0", pencolor="black", speed=10)
    t.fd(10)
    t.rt(90)
    t.fd(20)
    t.rt(90)
    t.fd(70)
    t.rt(90)
    t.fd(20)
    t.end_fill()
    t.rt(90)
    t.fd(10)
    t.rt(-90)
    t.fd(36)
    t.penup()


kémény(-124, 116)


def háztető22(x, y):
    t.penup()
    t.setposition(x, y)
    t.pen(pensize=1, fillcolor="red", pencolor="black", speed=10)
    t.begin_fill()
    t.pendown()
    t.rt(232)
    t.fd(180)
    t.rt(74)
    t.fd(155)
    t.rt(54)
    t.fd(167)
    t.rt(90)
    t.fd(247)
    t.rt(90)
    t.fd(162)
    t.end_fill()


háztető22(10, 41)


def háztető2(x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.rt(180)
    t.begin_fill()
    t.pen(pensize=2, fillcolor="brown", pencolor="black", speed=10)
    t.fd(24)
    t.bk(24)
    t.rt(54)
    t.fd(25)
    t.rt(92)
    t.fd(11)
    t.rt(87)
    t.fd(186)
    t.rt(73)
    t.fd(176)
    t.rt(79)
    t.fd(9)
    t.rt(101)
    t.fd(172)
    t.rt(-74)
    t.fd(180)
    t.end_fill()


háztető2(30, 57)


def ajtó(x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.begin_fill()
    t.pen(pensize=2, fillcolor="black", pencolor="black", speed=10)
    t.rt(128)
    t.fd(19)
    t.rt(90)
    t.fd(86)
    t.rt(90)
    t.fd(19)
    t.end_fill()
    t.bk(19)
    t.rt(90)
    t.fd(19)
    t.rt(90)
    t.begin_fill()
    t.pen(pensize=2, fillcolor="blue", pencolor="black", speed=10)
    t.fd(110)
    t.rt(-90)
    t.fd(50)
    t.rt(-90)
    t.fd(110)
    t.end_fill()


ajtó(96, -106)


def ajtóüveg(x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.begin_fill()
    t.pen(pensize=2, fillcolor="yellow", pencolor="black", speed=10)
    t.rt(45)
    t.fd(18)
    t.rt(-97)
    t.fd(18)
    t.rt(-85)
    t.fd(18)
    t.rt(-90)
    t.fd(18)
    t.end_fill()


ajtóüveg(137, 10)


def ablak3(x, y):
    t.penup()
    t.setposition(x, y)
    t.rt(47)
    t.pendown()
    t.begin_fill()
    t.pen(pensize=2, fillcolor="yellow", pencolor="black", speed=10)
    t.fd(35)
    t.rt(90)
    t.fd(60)
    t.rt(90)
    t.fd(35)
    t.rt(90)
    t.fd(60)
    t.end_fill()
    t.bk(30)
    t.rt(90)
    t.fd(35)
    t.bk(17)
    t.rt(90)
    t.fd(30)
    t.bk(60)


ablak3(196, -25)


def ablak4(x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.begin_fill()
    t.pen(pensize=2, fillcolor="yellow", pencolor="black", speed=10)
    t.rt(-90)
    t.fd(40)
    t.rt(-90)
    t.fd(55)
    t.rt(-90)
    t.fd(40)
    t.rt(-90)
    t.fd(55)
    t.end_fill()
    t.rt(-90)
    t.fd(20)
    t.rt(-90)
    t.fd(55)
    t.bk(27)
    t.rt(90)
    t.fd(20)
    t.bk(40)


ablak4(173, 78)
