from functools import reduce
import time

def fact_rec():
    while True:
        y = input("\nВведите не отрицательное целое число:")
        try:
            int(y)
        except ValueError:
            print("\nСори....НУЖНО ВВЕСТИ ЧИСЛО")
            continue
        else:
            y = int(y)
            if y < 0:
                print("\nНаписано же НЕ ОТРИЦАТЕЛЬНОЕ")
                continue
            else:
                break

    fact = lambda x: 1 if x == 0 else x * fact(x-1)
    print("Факториал числа {} равен ={}".format(y, fact(y)))
    time.sleep(2)
  

def fact_norec():
    while True:
        y = input("\nВведите не отрицательное целое число:")
        try:
            int(y)
        except ValueError:
            print("\nСори....НУЖНО ВВЕСТИ ЧИСЛО")
            continue
        else:
            y = int(y)
            if y < 0:
                print("\nНаписано же НЕ ОТРИЦАТЕЛЬНОЕ")
                continue
            else:
                break

    fact = reduce(lambda y,z:y*z,range(1,y+1))
    print("Факториал числа {} равен ={}".format(y, fact))
    time.sleep(2)


while True:
    f = input("""
Как будем вычислять факториал?
Лямбда С (Рекурсией)           -  1
Лямбда БЕЗ (Рекурсии)          -  2
Выход                          -  Enter
Что выбираем:""")

    if not f:
        print("Печалька...")
        time.sleep(1)
        break
    elif f == "1":
        fact_rec()
    elif f == "2":
        fact_norec()
    else:
        print("Повторите")
        time.sleep(3)
 
