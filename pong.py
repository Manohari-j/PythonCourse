import turtle

score_a = 0
score_b = 0
win = turtle.Screen()
win.setup(800, 600)
win.bgcolor("Orange")
win.title("Pong Game")
win.tracer(0)  # to avoid center to either side animation

# left paddle : w-up, s-down
left_paddle = turtle.Turtle()  # to create turtle object
left_paddle.speed(0)  # to avoid animation. 1- slow, 10 - fast
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_len=1, stretch_wid=5)
left_paddle.penup()  # to avoid the line while moving left
left_paddle.goto(-380, 0)

# right paddle: up arrow, down arrow
right_paddle = turtle.Turtle()  # to create turtle object
right_paddle.speed(0)  # to avoid animation. 1- slow, 10 - fast
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_len=1, stretch_wid=5)
right_paddle.penup()  # to avoid the line while moving left
right_paddle.goto(380, 0)

# ball

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.speed(0)
# dx, dy rate of change of ball movement
ball.penup()
ball.dx=0.15
ball.dy=0.15

# Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align = "center", font=("Ariel",24,"normal") )


# moving paddles
def left_paddle_up():
    newy = left_paddle.ycor() + 20
    if newy < 280:
        left_paddle.sety(newy)



def left_paddle_down():
    newy = left_paddle.ycor() - 20
    if newy > -280:
        left_paddle.sety(newy)
    # left_paddle.sety(left_paddle.ycor() - 20)


def right_paddle_up():
    newy = right_paddle.ycor() + 20
    if newy < 280:
        right_paddle.sety(newy)
    # right_paddle.sety(right_paddle.ycor() + 20)


def right_paddle_down():
    newy = right_paddle.ycor() - 20
    if newy > -280:
        right_paddle.sety(newy)
    # right_paddle.sety(right_paddle.ycor() - 20)


win.listen()
win.onkeypress(left_paddle_up, 'w')
win.onkeypress(left_paddle_down, 's')
win.onkeypress(right_paddle_up, 'Up')
win.onkeypress(right_paddle_down, 'Down')

while True:
    win.update()
    # ball movement automatically moves in x and y movement
    # to move the ball continuously in 1 px give inside loop
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    # ball-wall collision
    # if collided in right wall, A will get point and vice versa
    # top wall
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1 # to move down after hitting top wall
    # bottom wall
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    # right wall
    if ball.xcor()>390:
        ball.setx(390)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Ariel", 24, "normal"))

    # left wall
    if ball.xcor()<(-390):
        ball.setx(-390)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Ariel", 24, "normal"))

    # Collision with paddle
    if ball.xcor() > 370 and right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50:
        ball.setx(360)
        ball.dx *= -1
    if ball.xcor() < -370 and left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50:
        ball.setx(-360)
        ball.dx *= -1




