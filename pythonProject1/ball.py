from turtle import Turtle



ALIGNMENT = "center"
FONT =('Arial', 15, 'normal')
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(1)
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.ball_speed =0.1



    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *=0.9

    def reset_position(self):
        self.home()
        self.ball_speed =0.1
        self.bounce_x()



    def game_over(self):
        self.write("Game is Over",align=ALIGNMENT,font=FONT)