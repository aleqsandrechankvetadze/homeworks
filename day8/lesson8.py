from turtle import *

def draw_square():
    for i in range(4):
        forward(100)
        left(90)

# abstaction  აბსტრაქცია

draw_square()

penup()
goto(0, -300)
pendown()

draw_square()

penup()
goto(-300, -300)
pendown()

draw_square()

penup()
goto(-300, -0)
pendown()

draw_square()

exitonclick()
