from turtle import Turtle


class ScreenDivider(Turtle):
    def __init__(self):
        super(ScreenDivider, self).__init__()
        for y in range(300, -340, -40):
            d = Turtle(shape="square")
            d.penup()
            d.goto(0, y)
            d.color("white")
            d.turtlesize(stretch_wid=1, stretch_len=0.1)