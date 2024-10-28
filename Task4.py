def compute_f(n):
    def g(x, y):
        return ((y - 1) * x ** 5 + x ** 3 - x * y + 3 * x + 7 * y) % 9973

    if n == 0:
        return 0

    f = 0
    for i in range(1, n + 1):
        f = g(i, f)

    return f

n = int(input())
print(compute_f(n))

'''# 1375 нонконформизм
def solve(k, p):
    #словарь квадратов чисел по модулю
    squares = {i * i % p: i for i in range(p)}

    for x in range(p):
        #получаем квадрат y
        y_squared = (k - x * x) % p
        #Если нашел, то ищем значение корня и выводим заканчивая алгоритм
        if y_squared in squares:
            y = squares[y_squared]
            print(x, y)
            return

    print("NO SOLUTION")

k, p = map(int, input().split())
solve(k, p)'''