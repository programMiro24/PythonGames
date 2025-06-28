import random
game_characters = ["магик","принцеса","войн","дракон","еднорог"]
magik = [True, True, True, False, False]
princess = [False, True, True, False, True]
warrior = [False, False, True, True, True]
dragon = [True, True, False, True, False]
unicorn = [True, False, False, True, True]
game_wins = [magik,princess,warrior,dragon,unicorn]
count = 5
name = input("Enter nickname: ")
print(f"Welcome, {name}!")
ans = input(f"Do you want to play, {name}? (yes or no) ")
while ans=="yes":
    player_1 = int(input(f"Choose 1 for {game_characters[0]}, 2 for {game_characters[1]}, 3 for {game_characters[2]}, 4 for {game_characters[3]} and 5 for {game_characters[4]}: "))
    if player_1 > count or player_1 < 1:
        player_1=player_1%count+1
    print(f"{name} choose {game_characters[player_1-1]}")
         
    player_2 = random.randint(1,100000) % count + 1
    print(f"Computer choose {game_characters[player_2-1]}")
        
    if player_1 == player_2:
        print("Draw!")
    else:
        if game_wins[player_1-1][player_2-1]:
            print(f"{name} win. Computer lose.")
        else:
            print(f"{name} lose. Computer win.")
        
    ans = input(f"Do you want to play again, {name}? (yes or no) ")
print(f"Goodbye, {name}!")

