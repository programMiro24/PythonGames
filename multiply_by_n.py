multiply_number=int(input("Въведи числото, на което ще направя таблица за умножение: "))
for number in range(1,11):
    print(f"{multiply_number}.{number}={multiply_number*number}")