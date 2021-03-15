def read_from_file(filename="./text.txt"):
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data

while True:
    symbol = input("\nКакой символ хотите просчитать:")
    y = input("\nВведите текст-->") 

    if  not y:
       y = read_from_file()

    shet = sum(map(lambda x : 1 if symbol in x else 0, y)) 
    print("\nКоличество символов в введеном тексте:", str(shet))
   