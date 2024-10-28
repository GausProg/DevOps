'''def is_lucky_moscow(ticket):
    first_half = ticket[:len(ticket)//2]
    second_half = ticket[len(ticket)//2:]
    return sum(map(int, first_half)) == sum(map(int, second_half))

def is_lucky_spb(ticket):
    odd_sum = sum(map(int, ticket[::2]))
    even_sum = sum(map(int, ticket[1::2]))
    return odd_sum == even_sum

def count_unlucky_tickets(N):
    count = 0
    for ticket in range(10**N):
        ticket_str = str(ticket).zfill(N)
        if is_lucky_moscow(ticket_str) and is_lucky_spb(ticket_str):
            count += 1
    return count

N = int(input())
print(count_unlucky_tickets(N))'''
'''def is_lucky_spb(ticket):
    odd_sum = sum(map(int, ticket[::2]))
    even_sum = sum(map(int, ticket[1::2]))
    return odd_sum == even_sum
def count_unlucky_tickets(N):
    count = 0
    for first_half in range(10**(N//2)):
        first_half_str = str(first_half).zfill(N//2)
        second_half_sum = sum(map(int, first_half_str))
        for second_half in range(10**(N//2)):
            second_half_str = str(second_half).zfill(N//2)
            if sum(map(int, second_half_str)) == second_half_sum and is_lucky_spb(first_half_str+second_half_str):
                count += 1
    return count

N = int(input())
print(count_unlucky_tickets(N)'''

#Решение для задачи 1055 Сочетания
from math import factorial
from collections import Counter

# Функция для подсчета простых множителей числа n
def prime_factors_count(n):
    i = 2
    factors = Counter() # Создание объекта Counter для подсчета простых множителей
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i] += 1 # Увеличиваем счетчик последнего простого множителя
    if n > 1:
        factors[n] += 1
    return len(factors) #Возвращаем количество уникальных простых множителей числа n

# Функция для нахождения количества простых множителей числа C, вычисленного по формуле сочетаний
def find_prime_factors_count(N, M):
    C = factorial(N) // (factorial(M) * factorial(N - M))
    return prime_factors_count(C)

N, M = map(int, input().split())
print(find_prime_factors_count(N, M))





