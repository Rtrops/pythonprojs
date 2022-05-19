from turtle import  Screen, Turtle
import paddle
import ball
import scoreboard



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PING PONG")
screen.tracer(0)



first_paddle = paddle.Paddle((350, 0))
second_paddle = paddle.Paddle((-350, 0))
both_paddles = [first_paddle, second_paddle]
ball = ball.Ball()
l_score = scoreboard.Scoreboard((-100, 200))
r_score = scoreboard.Scoreboard((100, 200))




screen.listen()
screen.onkey(first_paddle.go_up, "Up")
screen.onkey(first_paddle.go_down, "Down")
screen.onkey(second_paddle.go_up, "w")
screen.onkey(second_paddle.go_down, "s")


game_on = True
while game_on:
    screen.update()
    ball.move_ball()
    
    # detect collision with wall top/bot
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #detect collision with paddle
    if ball.distance(first_paddle) < 50 and ball.xcor() > 320 or ball.distance(second_paddle) < 30 and ball.xcor() > -330:
        ball.ball_hit()

    #detect right paddle miss
    if ball.xcor() > 380:
        l_score.add_score()
        ball.reset_position()

    if ball.xcor() < -380:
        r_score.add_score()
        ball.reset_position()        
        





screen.exitonclick()


























