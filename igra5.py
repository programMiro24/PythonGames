import random
game_characters = ["магик","принцеса","войн","дракон","еднорог"]
magik = [True, True, True, False, False]
princess = [False, True, True, False, True]
warrior = [False, False, True, True, True]
dragon = [True, True, False, True, False]
unicorn = [True, False, False, True, True]
game_wins = [magik,princess,warrior,dragon,unicorn]
count = 5
wins_player = 0
wins_computer = 0
name = input("Enter nickname: ")
print(f"Welcome, {name}!")
ans = input(f"Do you want to play, {name}? (yes or no) ")
while ans=="yes":
    for ind in range(0,5):
        print(f"{ind} - {game_characters[ind]}")
    player_1 = int(input(f"Enter your choice: "))
    if player_1 > count or player_1 < 1:
        player_1=player_1%count+1
    print(f"{name} choose {game_characters[player_1]}")
         
    player_2 = random.randint(1,100000) % count + 1
    print(f"Computer choose {game_characters[player_2]}")
        
    if player_1 == player_2:
        print("Draw!")
    else:
        if game_wins[player_1-1][player_2-1]:
            print(f"{name} win. Computer lose.")
            wins_player += 1
        else:
            print(f"{name} lose. Computer win.")
            wins_computer += 1
    print(f"{name} wins are {wins_player} and computer wins are {wins_computer}.")
    ans = input(f"Do you want to play again, {name}? (yes or no) ") 
    while ans != "yes" and ans != "no":
       ans = input(f"Do you want to play again, {name}? (yes or no) ") 
    
    
print(f"Goodbye, {name}!")


