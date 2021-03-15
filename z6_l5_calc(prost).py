print("Для выхода нажмите Enter")
while True:
    otv = input("Знак (+,-,*,/): ")
    if not otv:
        break
    if otv in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if otv == '+':
            print("%.2f" % (x+y))
        elif otv == '-':
            print("%.2f" % (x-y))
        elif otv == '*':
            print("%.2f" % (x*y))
        elif otv == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")