"""name = input("Как се каваш? ")
print(f"Здравей, {name}!")"""
"""chislo1=int(input("Число 1 = "))
chislo2=int(input("Число 2 = "))
print(f"{chislo1}+{chislo2}={chislo1+chislo2}")
print(f"{chislo1}-{chislo2}={chislo1-chislo2}")
print(f"{chislo1}*{chislo2}={chislo1*chislo2}")
print(f"{chislo1}/{chislo2}={chislo1/chislo2}")
print(f"{chislo1}%{chislo2}={chislo1%chislo2}")
print(f"{chislo1}//{chislo2}={chislo1//chislo2}")
print(f"{chislo1}**{chislo2}={chislo1**chislo2}")"""

number = int(input("Въведете число: "))
ostatuk_na_2 = number%2
ostatuk_na_3 = number%3
ostatuk_na_5 = number%5
#ostatuk_na_7 = number%7
if ostatuk_na_2 == 0:
    print("Четно.")
else:
    print("Нечетно.")
    
if ostatuk_na_3 == 0 and ostatuk_na_5 == 0:
    print("Числото се дели на 3 и на 5")
else:
    print("Не се дели")
    
if ostatuk_na_3 == 0 or ostatuk_na_5 == 0:
    print("Числото се дели")
else:
    print("Не се дели")


