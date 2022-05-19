from ctypes import alignment
from turtle import Turtle, Screen
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')





class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.scoreboard = 0
        with open("./data.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 260)
        self.score_tracker()
        

    def score_tracker(self):
        self.clear()
        self.write(f"Score: {self.scoreboard} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

        

    def add_score(self):
        self.clear()
        self.scoreboard += 1
        self.score_tracker()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.scoreboard > self.high_score:
            self.high_score = self.scoreboard
            with open("./data.txt.", "w") as file:
                file.write(f"{self.high_score}") 
        self.scoreboard = 0
        self.score_tracker() 
        






