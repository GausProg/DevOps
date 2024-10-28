#1343 12 месяцев(НЕ ПОЛНОСТЬЮ РЕШИЛ)
import random

def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return 'NO', i
    return 'YES'


def miller_rabin(n, k=5):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for i in range(k):
        a = random.randint(2, n - 2)
        if not check(a, s, d, n):
            return False
    return True

flag = True
ans = 0
num = int(input())
months = int(input())*10**(12-num)
high = months+10**(12 - num)
while months < high and flag:
    if miller_rabin(months):
        ans = months
        flag = False
    else:
        months+=1
print(isprime(months))
print(months)

