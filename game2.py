import random
game_characters = ["магик","принцеса","войн","дракон","еднорог"]
count = 5
name = input("Enter nickname: ")
print(f"Welcome, {name}!")
ans = input(f"Do you want to play, {name}? (yes or no) ")
while ans=="yes":
    player_1 = int(input("Choose 1 for магик, 2 for принцеса, 3 for войн, 4 for дракон and 5 for еднорог: "))
    if player_1 > count or player_1 < 1:
        player_1=player_1%count+1
    print(f"{name} choose {game_characters[player_1-1]}")
         
    player_2 = random.randint(1,100000) % count + 1
    print(f"Computer choose {game_characters[player_2-1]}")
        
    if player_1 == player_2:
        print("Draw!")
    #win
    if player_1 == 1 and (player_2 == 2 or player_2 == 3):
        print(f"{name} win. Computer lose.")
    if player_1 == 2 and (player_2 == 3 or player_2 == 5):
        print(f"{name} win. Computer lose.")
    if player_1 == 3 and (player_2 == 4 or player_2 == 5):
        print(f"{name} win. Computer lose.")
    if player_1 == 4 and (player_2 == 1 or player_2 == 2):
        print(f"{name} win. Computer lose.")
    if player_1 == 5 and (player_2 == 1 or player_2 == 4):
        print(f"{name} win. Computer lose.")
    #lose
    if player_1 == 1 and (player_2 == 4 or player_2 == 5):
        print(f"{name} lose. Computer win.")
    if player_1 == 2 and (player_2 == 1 or player_2 == 4):
        print(f"{name} lose. Computer win.")
    if player_1 == 3 and (player_2 == 1 or player_2 == 2):
        print(f"{name} lose. Computer win.")
    if player_1 == 4 and (player_2 == 3 or player_2 == 5):
        print(f"{name} lose. Computer win.")
    if player_1 == 5 and (player_2 == 2 or player_2 == 3):
        print(f"{name} lose. Computer win.")
        
    ans = input(f"Do you want to play again, {name}? (yes or no) ")
print(f"Goodbye, {name}!")
