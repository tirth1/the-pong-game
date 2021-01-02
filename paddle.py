from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.score = 0
        
        if side == "left":
            self.goto(-350, 0)
        else:
            self.goto(350, 0)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)

    def goal(self):
        self.score += 1