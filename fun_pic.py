import turtle


def fun(x):
    return 0.01 * x * x - 2 * x + 10


turtle.screensize(700, 600, "white")
turtle.up()
turtle.goto(-600, 0)
turtle.down()
turtle.goto(600, 0)
turtle.goto(-600, 0)
turtle.up()
turtle.goto(0, 600)
turtle.down()
turtle.goto(0, -600)
turtle.up()
turtle.speed(0)
turtle.delay(0)
turtle.tracer(False)
i = -150.0
while 1:
    turtle.goto(i, fun(i))
    turtle.down()
    i = i + 0.001
    if (i > 350):
        break
# turtle.fillcolor("red")
# turtle.begin_fill()


# turtle.end_fill()
turtle.done()
