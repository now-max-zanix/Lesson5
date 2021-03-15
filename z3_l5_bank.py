while True:
    vznos = input("\nВнесите взнос:")
    try:
        float(vznos)
    except ValueError:
        print("ERROR-Вы ввели не число")
        continue
    else:
        vznos = float(vznos)
        if vznos < 0:
            print("Упс... Вклад не может быть отрицательным")
            continue
        else:
            break

while True:
    periud = input("На какой период оформляем вклад:")
    try:
        int(periud)
    except ValueError:
        print("ERROR-Вы ввели не число")
        continue
    else:
        periud = int(periud)
        if periud < 0:
            print("Фу... давайте без отризательных значений\n")
            continue
        else:
            break
    
while True:
    prozent = input("Под какой ежемесячный процент%:")
    try:
        float(prozent)
    except ValueError:
        print("ERROR-Вы ввели не число")
        continue
    else:
        prozent = float(prozent)
        if prozent < 0:
            print("Не может быть отрицательное значениe\n")
            continue
        else:
            break
    

def bank():
    kopilka = vznos*(prozent/100)*periud
    summa = kopilka + vznos
    print("\nВ копилку за {} месяцев  по ставке {}% поступило {:.2f} ".format(periud, prozent, kopilka))
    print("Итоговая сумма вклада:", summa)

bank()
