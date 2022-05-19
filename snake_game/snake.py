from turtle import Turtle


start_pos = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):    
        for each in start_pos:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(each)
            self.segments.append(new_segment)
    

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.new_x = self.segments[seg_num - 1].xcor()
            self.new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(self.new_x, self.new_y)
        self.head.fd(move_distance)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]    

    def add_tail(self):
        new_tail = Turtle("square")
        new_tail.penup()
        new_tail.color("white")
        new_tail.goto(self.new_x, self.new_y)
        self.segments.append(new_tail)
               
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)






            