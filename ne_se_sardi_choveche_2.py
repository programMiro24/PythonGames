import time
import random
import turtle
import sys
pionki = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
screen = turtle.Screen()
draw_1 = turtle.Turtle()
draw_1.shape("circle")
draw_1.width(4)
draw_1.penup()
draw_1.color("red")
draw_1.goto(-380, 160)
draw_1.pendown()
daljina_pole = 68
for tekushta_poziciq in range(1, daljina_pole + 1):
    draw_1.forward(5)
    draw_1.penup()
    draw_1.forward(5)
    draw_1.pendown()
pionki[0].shape("arrow")
pionki[0].color("red")
pionki[0].penup()
pionki[0].goto(-380, 200)

draw_2 = turtle.Turtle()
draw_2.shape("circle")
draw_2.width(4)
draw_2.penup()
draw_2.color("blue")
draw_2.goto(-380, 80)
draw_2.pendown()
for tekushta_poziciq in range(1, daljina_pole + 1):
    draw_2.forward(5)
    draw_2.penup()
    draw_2.forward(5)
    draw_2.pendown()
pionki[1].shape("arrow")
pionki[1].color("blue")
pionki[1].penup()
pionki[1].goto(-380, 120)

draw_3 = turtle.Turtle()
draw_3.shape("circle")
draw_3.width(4)
draw_3.penup()
draw_3.color("yellow")
draw_3.goto(-380, 0)
draw_3.pendown()

for tekushta_poziciq in range(1, daljina_pole + 1):
    draw_3.forward(5)
    draw_3.penup()
    draw_3.forward(5)
    draw_3.pendown()
pionki[2].shape("arrow")
pionki[2].color("yellow")
pionki[2].penup()
pionki[2].goto(-380, 40)

draw_4 = turtle.Turtle()
draw_4.shape("circle")
draw_4.width(4)
draw_4.penup()
draw_4.color("green")
draw_4.goto(-380, -80)
draw_4.pendown()

for tekushta_poziciq in range(1, daljina_pole + 1):
    draw_4.forward(5)
    draw_4.penup()
    draw_4.forward(5)
    draw_4.pendown()
pionki[3].shape("arrow")
pionki[3].color("green")
pionki[3].penup()
pionki[3].goto(-380, -40)

poziciq_pionki = [0, 0, 0, 0]
zars = [1, 1, 1, 1]
win = 0
game_over = False
while True:
    for index in range(4):
        if poziciq_pionki[index] >= daljina_pole:
            win = f"Gamer {index + 1}"
            game_over = True
    if game_over:
        break
    ans = input("Натисни Enter за игра.")
    for index in range(4):
        zars[index] = random.randint(1, 100000) % 6 + 1
        time.sleep(0.5)
    for index in range(4):
        print(f"Зар {index+1} = {zars[index]}")
        if poziciq_pionki[index] + zars[index] <= 68:
            poziciq_pionki[index] = poziciq_pionki[index]+zars[index]
        print(f"Позиция {index+1} = {poziciq_pionki[index]}")

    for index in range(4):
        if poziciq_pionki[index] <= 68:
            pionki[index].forward(zars[index] * 10)

print(f"{win} win!")
time.sleep(50)
sys.exit()
