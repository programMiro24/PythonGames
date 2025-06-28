import time
import random
import turtle
import sys
screen = turtle.Screen()
pole_1 = turtle.Turtle()
pole_1.shape("circle")
pole_1.width(4)
pole_1.penup()
pole_1.color("red")
pole_1.goto(-380, 160)
pole_1.pendown()
daljina_pole = 68
for tekushta_poziciq in range(1, daljina_pole + 1):
    pole_1.forward(5)
    pole_1.penup()
    pole_1.forward(5)
    pole_1.pendown()
pionka_1 = turtle.Turtle()
pionka_1.shape("arrow")
pionka_1.color("red")
pionka_1.penup()
pionka_1.goto(-380, 200)

pole_2 = turtle.Turtle()
pole_2.shape("circle")
pole_2.width(4)
pole_2.penup()
pole_2.color("blue")
pole_2.goto(-380, 80)
pole_2.pendown()
for tekushta_poziciq in range(1, daljina_pole + 1):
    pole_2.forward(5)
    pole_2.penup()
    pole_2.forward(5)
    pole_2.pendown()
pionka_2 = turtle.Turtle()
pionka_2.shape("arrow")
pionka_2.color("blue")
pionka_2.penup()
pionka_2.goto(-380, 120)

pole_3 = turtle.Turtle()
pole_3.shape("circle")
pole_3.width(4)
pole_3.penup()
pole_3.color("yellow")
pole_3.goto(-380, 0)
pole_3.pendown()

for tekushta_poziciq in range(1, daljina_pole + 1):
    pole_3.forward(5)
    pole_3.penup()
    pole_3.forward(5)
    pole_3.pendown()
pionka_3 = turtle.Turtle()
pionka_3.shape("arrow")
pionka_3.color("yellow")
pionka_3.penup()
pionka_3.goto(-380, 40)

pole_4 = turtle.Turtle()
pole_4.shape("circle")
pole_4.width(4)
pole_4.penup()
pole_4.color("green")
pole_4.goto(-380, -80)
pole_4.pendown()

for tekushta_poziciq in range(1, daljina_pole + 1):
    pole_4.forward(5)
    pole_4.penup()
    pole_4.forward(5)
    pole_4.pendown()
pionka_4 = turtle.Turtle()
pionka_4.shape("arrow")
pionka_4.color("green")
pionka_4.penup()
pionka_4.goto(-380, -40)

poziciq_pionka_1 = 1
poziciq_pionka_2 = 1
poziciq_pionka_3 = 1
poziciq_pionka_4 = 1

game_over = False
while True:
    for index in range(4):
        if poziciq_pionki[index] == daljina_pole:
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
