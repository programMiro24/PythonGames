import time
import random
import turtle
#gamer_1= turtle.Turtle()
#gamer_1.shape("triangle")
#gamer_1.width(4)
pionka=[turtle.Turtle(),turtle.Turtle(),turtle.Turtle(),turtle.Turtle()]

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
    

pionka[0].shape("arrow")
pionka[0].color("red")
pionka[0].penup()
pionka[0].width(4)
pionka[0].goto(-380,200)


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
    

pionka[1].shape("arrow")
pionka[1].color("blue")
pionka[1].penup()
pionka[1].width(4)
pionka[1].goto(-380,120)

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
    

pionka[2].shape("arrow")
pionka[2].color("yellow")
pionka[2].penup()
pionka[2].width(4)
pionka[2].goto(-380,40)

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
    

pionka[3].shape("arrow")
pionka[3].color("green")
pionka[3].penup()
pionka[3].width(4)
pionka[3].goto(-380,-40)

pozizia_players=[0,0,0,0]


zars=[1,1,1,1]

pionka_1_pozicia=1
zar1=1
pionka_2_pozicia=1
zar2=1
pionka_3_pozicia=1
zar3=1
pionka_4_pozicia=1
zar4=1
game_over=False
while True:
    
    for index in range(0,4):   
        if pozizia_players[index]==daljina_pole:
            win="Gamer"+str(index+1)
            game_over=True
    if game_over:
        break
           
    ans=input("Natisni Enter za Game")
    for index in range(0,4):
        zars[index]=random.randint(1,100000)%6+1
        time.sleep(0.5)
    for index in range(0,4):
        print(f"ZAR{index}= {zars[index]}")
        if pozizia_players[index]+zars[index]<=68:
           pozizia_players[index]=pozizia_players[index]+zars[index]
        print(f"pozicia{index}= {pozizia_players[index]}")
     
    
    for index in range(0,4):
        if pozizia_players[index]<=68:
            pionka[index].forward(zars[index]*10)
    
    


print(f"{win} WIN!!!")
    