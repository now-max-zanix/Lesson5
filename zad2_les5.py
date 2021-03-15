import re
import time

def read_from_file(filename="./text.txt"):
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data

def col_pred():
    text = input("\nВведите текст:(Enter-для чтения файла):")
    if not text:
        text = read_from_file()
    new = re.sub(r'[.!?]\s', r'|', text)
    predl = len(new.split('|')) 
    print("Количество предложений:(. и пробел(конец предложения))", predl)
    time.sleep(2)


def col_symbol():
    text = input("\nВведите текст:(Enter-для чтения файла):")
    if not text:
        text = read_from_file()

    fso = {}

    for symbol in text:
        fso[symbol] = fso.get(symbol, 0) + 1
    
    for key in sorted(fso):
        print(f'{key} : {fso[key]}')
    time.sleep(2)

def col_word():
    text = input("\nВведите текст:(Enter-для чтения файла):")
    if not text:
        text = read_from_file()

    text = text.replace("!", " ")
    text = text.replace("?", " ")
    text = text.replace(".", " ")
    text = text.replace(",", " ")
    text = text.replace("\n", " ")
    text = text.split()
    word = len(text)
    print("Количество слов:", word)
    time.sleep(2)

while True:
    g = input("""
Количество слов        - 1
Количество предложений - 2
Частота символов       - 3
Выход                  -  Enter
Что выбрали: """)
    if not g:
        print("Печалька...")
        time.sleep(1)
        break
    elif g == "1":
        col_word()
    elif g == "2":
        col_pred()
    elif g == "3":
        col_symbol()
    else:
        print("Повторите")
        time.sleep(3)
