# День 2: Циклы (for, while) и генераторы
from traceback import print_tb

# Практика:

def one(a):
    # Написать цикл for, который выводит все четные числа из списка.
    arr = []
    for i in a:
        if i%2==0:
            arr.append(i)
    print(*arr)
a = [0,1,2,3,4,5,6,7,8,9]
one(a)

# Создать генератор списка, который возводит числа от 1 до 10 в квадрат.
print(*[b**2 for b in a]) # генератор списка хранит все в памяти
print(*(b**2 for b in a)) # а это просто генератЖЖор который ничего не хранит в памяти

def kek(word):
    # Реализовать цикл while, который принимает пользовательский ввод, пока не
    # введено слово "стоп".
    while word != 'stop':
        word = input('ввод: ')
    print('loop break')

# kek(input('ввод: '))
#
# Домашнее задание:
# Создать словарь через генератор, где ключи — это числа от 1 до 10, а значения — их кубы.
print(*({k : k**3 } for k in a)) # это именно генератор, а не генератор списков