# День 3: Условные операторы (if, elif, else)

# Практика:

def rang(i,num):
    # Написать функцию, которая проверяет, входит ли число в заданный диапазон, используя if.
    print(i in [a for a in range(num[0], num[1]+1)])

def hundred(arr):
    # Использовать any() для проверки, есть ли в списке числа больше 100.
    print(any(a>100 for a in arr))

def double(x, y):
    # Написать программу, которая принимает два числа и сравнивает их(равны, больше, меньше).
    print(f'{x}>{y}' if x>y else f'{x}<{y}' if x<y else f'{x}=={y}')

num = (1,10)
rang(2,num)
hundred([1,2,3,4,105])
double(10,4)

# Домашнее задание:

def five(arr):
    # Реализовать функцию, которая проверяет, можно ли составить из элементов списка числа, делящиеся на 5.
    print(any(a%5==0 for a in arr))

five([1,2,3,4,5,6,25,50])
