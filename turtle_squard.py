import turtle

tina = turtle.Turtle()
tina.shape("circle")
tina.color("pink")
tina.width(4)
tina.penup()
tina.goto(0,60)
tina.pendown()

tommy = turtle.Turtle()
tommy.penup()
tommy.shape("circle")
tommy.color("cyan")
tommy.goto(-50,-90)
tommy.width(4)
tommy.left(90)
tommy.pendown()

for i in range(10):
    for j in range(4):
        tina.right(90)
        tommy.right(90)
        tina.forward(130)
        tommy.forward(75)
    #tommy.write(f"{i+1} done,{4-i} to go!", None, None, "12pt bold")
    tommy.right(36)
    tina.right(36)
"""
tommy.goto(-55,-175)
#tommy.write("Great job, Tina!", None, None, "16pt bold")
tina.color("purple")
tommy.goto(-75,-175)
tina.penup()
tina.forward(40)
#tina.write("Thanks!", None, None, "16pt bold")
tina.backward(40)
"""