#Adham's First Project
import turtle
import winsound
wn = turtle.Screen()
wn.title("Pong :By Adham Zineldin")
wn.bgcolor("black")
wn.setup(width=800 , height=600)
wn.tracer(0)
#score
score_a = 0
score_b = 0
#paddle 1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
#paddle 2
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(" Player 1: 0   Player 2: 0", align="center", font=("courie", 24, "normal"))
#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 60
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 60
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 60
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 60
    paddle_b.sety(y)
#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
#main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("PLayer 1: {}   PLayer 2: {}".format(score_a, score_b), align="center", font=("courie", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("PLayer 1: {}   PLayer 2: {}".format(score_a, score_b), align="center", font=("courie", 24, "normal"))

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 55 and ball.ycor() > paddle_b.ycor() -55):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 55 and ball.ycor() > paddle_a.ycor() -55):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)