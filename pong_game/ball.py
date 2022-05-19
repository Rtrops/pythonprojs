from turtle import Turtle
from random import randint

START_X_Y = (0,0)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("slowest")
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = .2
        self.y_move = .2



    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def ball_hit(self):    
        self.x_move *= -1
        self.y_move *= -1


    def reset_position(self):
        self.goto(0,0)
        self.ball_hit()