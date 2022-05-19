from turtle import Turtle


class GuessTheState(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def right_answer(self, state, x, y):
        self.goto(x, y)
        self.write(f"{state.capitalize()}", align="center", font=("Courier", 10, "normal"))
