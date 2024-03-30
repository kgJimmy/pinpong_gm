import turtle as  t
import random
import time

def psright():
    if bar.xcor() < 180:
        bar.forward(15)



def psleft():
    if bar.xcor() > -180:
        bar.back(15)

t.bgcolor("lightblue")
t.setup(500, 700)


bar = t.Turtle()
bar.shape("square")
bar.shapesize(1, 6)
bar.up()
bar.speed(0)
bar.color("coral")
bar.goto(0, -270)

ball = t.Turtle()
ball.shape("circle")
ball.shapesize(1.1)
ball.up()
ball.speed(0)
ball.color("black")





t.listen()
t.onkeypress(psleft, "Left")
t.onkeypress(psright, "Right")

ball_xspeed = 5
ball_yspeed = 5
game_start = True

HP = 3
t.up
t.ht()
t.penup()
t.goto(0, 300)
t.write(f"Heart: {HP}", False, "center", ("", 20))

while True:
    new_x = ball.xcor() +ball_xspeed
    new_y = ball.ycor() +ball_yspeed
    ball.goto(new_x, new_y)

    if ball.xcor() > 240  or  ball.xcor() < -240:
        ball_xspeed *= -1

    if ball.ycor() > 340:
        ball_yspeed *= -1

    if ball.ycor() < -340:
        HP -= 1
        t.clear()
        t.write(f"Heart: {HP}", False, "center", ("", 20))
        time.sleep(0.7)
        ball.goto(0,100)
        ball_yspeed *= -1
        ball_xspeed *= -1

        if HP ==0:
            game_start = False
            t.goto(0,0)
            t.write("Game over", False, "center", ("", 20))


    if bar.distance(ball) < 50 and -260 < ball.ycor() < -245:
        ball_yspeed *= -1







t.done()