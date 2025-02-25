# День 5: Декораторы
# Декоратор @classmethod превращает метод в метод класса
# Декоратор @staticmethod превращает метод в статический метод.
# @abstractmethod: Для обозначения методов, которые должны быть реализованы в дочерних классах.
middleware = [1,2,3,4,5,6]


def benchmark(middleware):
    def decorator(func):
        import time

        def wrapper(*args, **kwargs):
            start = time.time()

            for arg in args:
                if arg not in middleware:
                    end = time.time()
                    print(f'[*] Время выполнения {func.__name__}: {end - start} секунд.')
                    return "404"

            return_value = func(*args, **kwargs)
            end = time.time()
            print(f'[*] Время выполнения {func.__name__}: {end - start} секунд.')
            return return_value

        return wrapper

    return decorator

middleware = [1, 2, 3, 4, 5]

@benchmark(middleware)
def tg(id):
    return "Success"

print(tg(10))
print(tg(3))