from turtle import Turtle
from paddle import Paddle
ALIGNMENT = "center"
FONT =('Arial', 20, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.update_scoreboard()




    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 260)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 260)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)


    def left_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def right_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

