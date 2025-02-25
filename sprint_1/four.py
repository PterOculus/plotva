# День 4: ООП и магические методы

# Магические методы:
# __init__ - инициализации атрибутов объекта
# __str__ - возвращает строковое представление объекта
# __len__ - возвращает длину объекта
# __add__ - определяет поведение оператора сложения
# __getitem__ - позволяет объекту поддерживать индексацию

class Book:
    # Создать класс для описания книги(атрибуты: название, автор).
    # Добавить метод __str__, который возвращает строку.

    def __init__(self, name, author):
        self.name = name
        self.author = author


    def __str__(self):
        return f"Name: {self.name}\nAuthor: {self.author}"

book_1 = Book("python", "Karl")

print(book_1)

class Plus:
    # Реализовать класс, который поддерживает сложение двух объектов через метод __add__.
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __add__(self, another):
        first = another.first + self.first
        second = another.second + self.second

        return (f"{self.first} + {another.first} = {first}\n"
                f"{self.second} + {another.second} = {second}\n"
                f"{first} + {second} = {first + second}")

num = Plus(1,2)
num_2 = Plus(3, 4)

print(num_2+num)

class InvalidList:

    def __init__(self, items):
        self.items = items

    def __getitem__(self, i):
        return self.items[i]

arr = InvalidList([1,2,3,4,5])
print(arr[3])