from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self, coords):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(coords)
        self.write(self.score, align="center", font=("Courier", 80, "normal")) 

        

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, align="center", font=("Courier", 80, "normal")) 
        
