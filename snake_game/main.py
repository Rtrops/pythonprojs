from turtle import Screen
import time
import snake
from food import Food
import scoreboard


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY ANACONDA DON'T")

snakey = snake.Snake()
foody = Food()
score = scoreboard.Scoreboard()




screen.listen()
screen.onkey(snakey.up,"Up")
screen.onkey(snakey.down,"Down")
screen.onkey(snakey.left,"Left")
screen.onkey(snakey.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snakey.move()

    #detect collision with food
    if snakey.head.distance(foody) < 15:
        foody.refresh()
        score.add_score()
        snakey.add_tail()

    #detect collision with wall.
    if snakey.head.xcor() > 280 or snakey.head.xcor() < -280 or snakey.head.ycor() > 290 or snakey.head.ycor() < -280:
        score.reset()
        snakey.reset()
    #detect collision with tail
    for segment in snakey.segments[1:]:
        if snakey.head.distance(segment) < 10:
            score.reset()
            snakey.reset()






screen.exitonclick()