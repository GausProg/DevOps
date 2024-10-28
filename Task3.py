#1366 подарки
def derangement(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    if n == 2:
        return 1

    prev_prev = 0
    prev = 1

    for i in range(3, n + 1):
        current = (i - 1) * (prev + prev_prev)
        prev_prev = prev
        prev = current


    return current


n = int(input())
result = derangement(n)
print(result)
