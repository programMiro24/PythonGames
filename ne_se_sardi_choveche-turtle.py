import time
import random
import turtle
#gamer_1= turtle.Turtle()
#gamer_1.shape("triangle")
#gamer_1.width(4)
pole_1= turtle.Turtle()
pole_1.shape("circle")
pole_1.penup()
pole_1.width(4)
pole_1.goto(-380,160)
pole_1.pendown()
pole_1.color("red")
daljina_pole=68
for pozicia in range(1,daljina_pole+1):
    pole_1.forward(5)
    #pole_1.write(f"{pozicia}", False, align="center")
    pole_1.penup()
    pole_1.forward(5)
    pole_1.pendown()
    
pionka_1=turtle.Turtle()
pionka_1.shape("arrow")
pionka_1.color("red")
pionka_1.penup()
pionka_1.width(4)
pionka_1.goto(-380,200)


pole_2= turtle.Turtle()
pole_2.shape("circle")
pole_2.penup()
pole_2.width(4)
pole_2.goto(-380,80)
pole_2.pendown()
pole_2.color("blue")

for pozicia in range(1,daljina_pole+1):
    pole_2.forward(5)
    #pole_1.write(f"{pozicia}", False, align="center")
    pole_2.penup()
    pole_2.forward(5)
    pole_2.pendown()
    
pionka_2=turtle.Turtle()
pionka_2.shape("arrow")
pionka_2.color("blue")
pionka_2.penup()
pionka_2.width(4)
pionka_2.goto(-380,120)

pole_3= turtle.Turtle()
pole_3.shape("circle")
pole_3.penup()
pole_3.width(4)
pole_3.goto(-380,0)
pole_3.pendown()
pole_3.color("yellow")

for pozicia in range(1,daljina_pole+1):
    pole_3.forward(5)
    #pole_1.write(f"{pozicia}", False, align="center")
    pole_3.penup()
    pole_3.forward(5)
    pole_3.pendown()
    
pionka_3=turtle.Turtle()
pionka_3.shape("arrow")
pionka_3.color("yellow")
pionka_3.penup()
pionka_3.width(4)
pionka_3.goto(-380,40)

pole_4= turtle.Turtle()
pole_4.shape("circle")
pole_4.penup()
pole_4.width(4)
pole_4.goto(-380,-80)
pole_4.pendown()
pole_4.color("green")

for pozicia in range(1,daljina_pole+1):
    pole_4.forward(5)
    #pole_1.write(f"{pozicia}", False, align="center")
    pole_4.penup()
    pole_4.forward(5)
    pole_4.pendown()
    
pionka_4=turtle.Turtle()
pionka_4.shape("arrow")
pionka_4.color("green")
pionka_4.penup()
pionka_4.width(4)
pionka_4.goto(-380,-40)
'''zar1=random.randint(1,6)
while zar1<6:
    zar1=random.randint(1,6)
    print(f"ZAR= {zar1}")'''
pionka_1_pozicia=1
zar1=1
pionka_2_pozicia=1
zar2=1
pionka_3_pozicia=1
zar3=1
pionka_4_pozicia=1
zar4=1

while True:
    
        
    if pionka_1_pozicia==daljina_pole:
        win="Gamer 1"
        break
    if pionka_2_pozicia==daljina_pole:
        win="Gamer 2"
        break
    
    if pionka_3_pozicia==daljina_pole:
        win="Gamer 3"
        break
    if pionka_4_pozicia==daljina_pole:
        win="Gamer 4"
        break
    
    ans=input("Natisni Enter za Game")
    
    zar1=random.randint(1,100000)%6+1
    time.sleep(0.5)
    print(f"ZAR1= {zar1}")
    if pionka_1_pozicia+zar1<=68:
       pionka_1_pozicia=pionka_1_pozicia+zar1
     
    zar2=random.randint(1,100000)%6+1
    time.sleep(0.5)
    print(f"ZAR2= {zar2}")
    if pionka_2_pozicia+zar2<=68:
       pionka_2_pozicia=pionka_2_pozicia+zar2       
    
    zar3=random.randint(1,100000)%6+1
    time.sleep(0.5)
    print(f"ZAR3= {zar3}")
    if pionka_3_pozicia+zar3<=68:
       pionka_3_pozicia=pionka_3_pozicia+zar3
    
    zar4=random.randint(1,100000)%6+1
    time.sleep(0.5)
    print(f"ZAR4= {zar4}")
    if pionka_4_pozicia+zar4<=68:
       pionka_4_pozicia=pionka_4_pozicia+zar4
    
    pionka_1.forward(zar1*10)
    pionka_2.forward(zar2*10)
    pionka_3.forward(zar3*10)
    pionka_4.forward(zar4*10)


print(f"{win} WIN!!!")
    
