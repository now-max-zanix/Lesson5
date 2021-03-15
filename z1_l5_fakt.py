while True:
    x = input("\nВведите не отрицательное целое число:")
    try:
        int(x)
    except ValueError:
        print("\nСори....НУЖНО ВВЕСТИ ЧИСЛО")
        continue
    else:
        x = int(x)
        if x < 0:
            print("\nНаписано же НЕ ОТРИЦАТЕЛЬНОЕ")
            continue
        else:
            break

def factoril():
    fac = 1
    if x == 0:
         print("\nРезультат:", fac)
    else:
        for i in range(1, x+1):
            fac *= i 
        print("\nРезультат:", fac)
        
factoril()