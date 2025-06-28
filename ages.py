age = int(input("Въведи своята възраст: "))
if age>0:
    if age<=6:
        print("Ти си в детската градина")
    elif age<=10:
        print("Ти си в началното училище")
    elif age<=14:
        print("Ти си в прогимназията")
    elif age<=19:
        print("Ти си в гимназията")
    else:
        print("Ти си завършил")
else:
    print("Не си роден!")