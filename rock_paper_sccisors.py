import random
name = input("Enter nickname: ")
print(f"Welcome, {name}!")
ans = input(f"Do you want to play, {name}? (yes or no) ")
wins_player = 0
wins_computer = 0
while ans=="yes":
    player_1 = int(input("Choose 1 for rock, 2 for paper and 3 for scissors: "))
    if player_1 > 3 or player_1 < 1:
        player_1=player_1%3+1
    if player_1 == 1:
        print(f"{name} choose rock")
    if player_1 == 2:
        print(f"{name} choose paper")
    if player_1 == 3:
        print(f"{name} choose scissors")
        
    player_2 = random.randint(1,10000) % 3 + 1
    if player_2 == 1:
        print("Computer choose rock")
    if player_2 == 2:
        print("Computer choose paper")
    if player_2 == 3:
        print("Computer choose scissors")
        
    if player_1 == player_2: #Равенство на играчите и уравновесяването на резултатите
        print("Draw!")
    if player_1 == 1:#камък
        if player_2 == 2:#хартия
            print(f"{name} lose. Computer win.")
            wins_computer += 1
        if player_2 == 3:#ножица
            print(f"{name} win. Computer lose.")
            wins_player += 1

    if player_1 == 2:#хартия
        if player_2 == 1:#камък
            print(f"{name} win. Computer lose.")
            wins_player += 1
        if player_2 == 3:#ножица
            print(f"{name} lose. Computer win.")
            wins_computer += 1
            
    if player_1 == 3:#ножица
        if player_2 == 1:#камък
            print(f"{name} lose. Computer win.")
            wins_computer += 1
        if player_2 == 2:#хартия
            print(f"{name} win. Computer lose.")
            wins_player += 1
    print(f"Your wins are {wins_player} and computer wins are {wins_computer}.")
    ans = input(f"Do you want to play again, {name}? (yes or no) ") 
    while ans != "yes" and ans != "no":
       ans = input(f"Do you want to play again, {name}? (yes or no) ") 
print(f"Goodbye, {name}!")
