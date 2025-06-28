import random
computer_number = random.randint(1,100000000)%11
player_number = int(input("Въведете своето предположение: "))
opiti = 1
while computer_number == player_number:
    opiti+=1
    player_number = int(input("Въведете своето предположение: "))
print("Отлична игра")
print(f"Позна числото с {opiti} опита.")