from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, side):
        super(Scoreboard, self).__init__()
        self.shape("square")
        self.hideturtle()
        self.penup()
        if side == "left":
            self.goto(-120, 230)
        else:
            self.goto(120, 230)
        self.color("white")

    def score(self, score):
        self.clear()
        self.write(f"{score}", align="center", font=("Arial", 70, "normal"))