import time
import random
daljina_pole = 68
zarcho = random.randint(1,6)
while zarcho<6:
    zarcho = random.randint(1,6)
    print(f"ZAR = {zarcho}")
moyata_pozicia = 1
while True:
    for tekushta_poziciq in range(1,daljina_pole+1):
        if tekushta_poziciq==moyata_pozicia:
            print(f"i{tekushta_poziciq}",end=" ")
        else:
            print(f"_{tekushta_poziciq}",end=" ")
        #time.sleep(0.50)
    print("")
    if moyata_pozicia==daljina_pole:
        break
    zar = random.randint(1,6)
    print(f"Zar = {zar}")
    if moyata_pozicia + zar <= daljina_pole:
        moyata_pozicia += zar
print("You win!")