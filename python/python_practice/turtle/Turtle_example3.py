# demonstrate the logo of EEcamp
# EvolvE
# 土法煉鋼!
import turtle as tt
tt.screensize(canvheight=1200, canvwidth=1600)
tt.speed(10)

def curve(iter, angle, length=5):
    for i in range(iter):
        tt.right(angle)
        tt.forward(length)
def fishtail():
    tt.penup()
    tt.pencolor("light salmon")
    tt.pensize(30)
    tt.setheading(-205)
    tt.sety(0)
    tt.setx(-400)
    tt.pendown()
    curve(24, -10, 20)
    tt.penup()
    tt.setposition(-534.66,-112.99)
    tt.pencolor("aqua")
    tt.pendown()
    tt.right(30)
    tt.forward(100)
def v():
    tt.penup()
    tt.forward(90)
    tt.pendown()
    tt.setheading(300)
    tt.forward(90)
    tt.setheading(45)
    curve(4, -10, 25)
def o():
    tt.penup()
    tt.setheading(0)
    tt.forward(80)
    tt.setheading(190)
    tt.pendown()
    tt.circle(40)
def l():
    tt.penup()
    tt.setheading(55)
    tt.forward(130)
    tt.setheading(-45)
    tt.pendown()
    curve(10, 3)
    curve(28, 0.5)
    curve(4, 5)
def fin():
    tt.penup()
    tt.setheading(55)
    tt.forward(130)
    tt.pencolor('light salmon')
    tt.pendown()
    tt.setheading(280)
    curve(10, 0.5, 10)
    curve(20, 1)
    tt.setheading(30)
    for i in range(50):
        tt.left((5-0.06*i)/5)
        tt.forward(5)
def face():
    tt.penup()
    tt.setposition(240, 60)
    tt.setheading(25)
    tt.pendown()
    curve(50, 5, 15)
    tt.penup()
    tt.pencolor("aqua")
    tt.setposition(300, -20)
    tt.pendown()
    tt.setheading(270)
    tt.forward(20)
    tt.penup()
    tt.setposition(320, -100)
    tt.pendown()
    tt.setheading(-30)
    curve(30, -2)
def wave():
    tt.penup()
    tt.pencolor("aqua")
    tt.setposition(-534, 140)
    tt.pendown()
    for i in range(7):
        if i == 0 or i == 6:
            tt.pencolor('light salmon')
            tt.setheading(-30)
            curve(30, -2)
        else:
            tt.setheading(-30)
            curve(30, -2)
def sharkfin():
    tt.penup()
    tt.setposition(-40, 170)
    tt.setheading(115)
    tt.pencolor("light salmon")
    tt.pendown()
    tt.setheading(80)
    curve(10, -1, 10)
    curve(10, -1)
    tt.setheading(-30)
    for i in range(40):
        tt.right((4-0.08*i)/5)
        tt.forward(5)
fishtail()
v()
o()
l()
fin()
face()
wave()
sharkfin()
tt.done()