# P1

# l = [5, 10, 15, 20, 25, 50, 20]
# x = l.index(20)
#
# if 20 in l:
#     l.pop(x)
#     l.insert(x, 200)
# print(l)

# P2

# l_1 = [5, 20, 15, 20, 25, 50, 20]
# y = l_1.index(20)
#
# if 20 in l_1:
#     l_1.pop(y)
#     print(l_1)

# P3
"""
n = int(input())
l_2 = []
for i in range(n):
    l_2.append(int(input()))
s = set(l_2)
s1 = list(l_2)
s1.sort(reverse=True)
print(s1[1])
"""
# P4

# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dic4 = {}
# dic4.update(dic1)
# dic4.update(dic3)
# dic4.update(dic2)
# print(dic4)

# P5

# dic_remove1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# dic_remove1.pop('a')
# print(dic_remove1)
#
# dic_remove2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# if 'e' in dic_remove2:
#     dic_remove2.pop('e')
# else:
#     print(dic_remove2)

# P6
#
# s = {1, 10, 90, 9}
# n = 90
# if n in s:
#     print(True)
#
# # P7
#
# n = int(input())
# i = 0
# while i + 7 <= n:
#     i = i + 7
#     print(i)

# Homework 3 ---------------------------------------------------------------------

# Salaries
# version1

# number_of_employees = int(input('The number of employees: '))
# salaries = []
#
# for i in range(number_of_employees):
#     salaries.append(int(input('Enter the salary: ')))
#     salaries.sort()
# difference = salaries[-1] - salaries[0]
#
# print(f'The difference is:  {difference}')


# Version 2

# number_of_employees = int(input('The number of employees: '))
# salaries = []
#
# for i in range(number_of_employees):
#     salaries.append(int(input('Enter the salary: ')))
# difference = max(salaries) - min(salaries)
#
# print(f'The difference is:  {difference}')


# Boring numbers
"""
number = int(input())
number_list = []
value = "Boring"
if number // 10 != 0:
    while number // 10 != 0:
        number_list.append(number % 10)
        number = number // 10
number_list.append(number)

for i in number_list[1:]:
    first = number_list[0]
    if i != first:
        value = "Interesting"
        break

print(value)
"""


# Largest Number
# version 1

"""
number = int(input())
number_list = []
value = "No"

if number // 10 !=0:
    while number // 10 != 0:
        number_list.append(number % 10)
        number = number // 10
number_list.append(number)
right_list = number_list[-1::-1]
print(right_list)
number_list.sort(reverse=True)    # ???????????? ???????? ???? ???????????????? 

def my_sum(*args):
    result = 0

    for x in args:
        result += x
    return result


l_number = input()
answer = "No"

if len(l_number) != 1:
    lst = list(l_number)
    lst.sort(reverse=True)

print(answer)
"""

# Largest number 2

# x = int(input())
#
# while x > 0:
#     if x < 10:
#         print("No")
#         break
#     elif (x % 10) > ((x // 10) % 10):
#         print("Yes")
#         break
#     else:
#         x = x // 10

# Line Segment Intersection

"""
a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())


if a1 > b1:
    a1, b1 = b1, a1
if a2 > b2:
    a2, b2 = b2, a2

if a2 > b1 or a1 > b2:
    print(0)
elif a1 <= a2 < b1 <= b2:  # 1, 2.5, 3, 2
    print(b1 - a2)
elif a2 <= a1 < b2 < b1:   # 3, 2, 1, 2.5
    print(b2 - a1)
elif a1 == a2 and b1 == b2:
    print(b1 - a2 + 1)
elif a1 >= a2 and b1 <= b2: # 10, 0, 0.1, 0.2
    print(b1 - a1)
elif a2 >= a1 and b2 <= b1: # 0.1, 0.2, 10, 0
    print(b2 - a2)
"""

#  Number Of Divisors
"""
x = int(input())
divisors = 0

for i in range(1, x+1):
    if x % i == 0:
        divisors += 1
print(divisors)
"""

#  Quadratic Equation

# from math import sqrt
# a = float(input())
# b = float(input())
# c = float(input())
#
#
# if a == 0:
#     print("Non-quadratic equation")
#     if b != 0:
#         x1 = c/(-b)
#         print(x1)
#     elif b == 0 and c != 0:
#         print("No solutions")
#     else:
#         print("Infinite solution")
# if a != 0:
#     print("Quadratic equation")
#     D = b ** 2 - 4 * a * c
#     print(f"Discriminant: {D}")
#     if D < 0:
#         print("No solutions")
#     if D == 0:
#         x1 = (-b + sqrt(D)) / 2 * a
#         print(f"One solution  {x1}")
#     if D > 0:
#         x1 = (-b + sqrt(D))/2*a
#         x2 = (-b - sqrt(D))/2*a
#         print(f"Two solutions: {x1}, {x2} ")


# List 1
"""
lst = ['a', 'b', 'c', 'd']

listToStr = ''.join(map(str, lst))

print(listToStr)
"""

# # List 2
#
# lst = [1, 1, 1, 0, 0, 0, 2, -2, -2]
# # set_1 = set(lst)
# # lst_1 = list(set_1)
# # lst_1.sort()
# # print(lst_1[1])
#
# min1 = lst[0]
# min2 = lst[1]
#
# for el in lst:
#     if el < min1:
#         min2 = min1
#         min1 = el
#     elif min1 < el < min2:
#         max2 = el
#
# print(min2)

#  Homework 4 ------------------------------------------------------------------

# Index Sum

# N = int(input('Enter N parameter: '))
# seq_a = []
# seq_ind = []
# for i in range(N):
#     seq_a.append(float(input()))
# M = int(input("Enter M parameter: "))
# for i in range(M):
#     seq_ind.append(int(input()))
#
# my_sum = 0
#
# for i in seq_ind:
#     my_sum += seq_a[i]
# print(my_sum)

# The most divisor-rich number


def divisor(x):
    divisors = 0
    for i in range(1, x+1):
        if x % i == 0:
            divisors += 1
    return divisors

# a = int(input())
# b = int(input())
# most_div = a
# for j in range(a, b+1):
#     if divisor(j) > divisor(most_div):
#         most_div = j
#
# print(most_div)


# Tree

# numb_of_star = int(input())
# bs = 0
# for i in range(1, numb_of_star+1):
#     if i % 2 == 1:
#         bs = int((numb_of_star-i)/2)
#         print((bs * ' '), i * "*", (bs * ' '))
#
#
# for i in range(1, numb_of_star+1, 2):
#     bs = int((numb_of_star-i)/2)
#     print((bs * ' '), i * "*", (bs * ' '))


#  The Goldbach Conjecture

def prime(x):
    switch = False
    for i in range(2, x // 2):
        if x % i == 0:
            switch = True
    if switch:
        return 0
    else:
        return 1


n = int(input())
z = 0
for j in range(2, n):
    if prime(j) == 1:
        z = n - j
        if prime(z) == 1:
            print(j, z)
            break


# Palindrome numbers

x = str(input())
y = str(input())
for i in range(int(x), int(y)):
    x = str(i)
    if int(x[-1::-1]) - int(x) == 0:
        print(x)

# Suffix Sums

A = [1.5, 2.5, 3]
B = []

for i in range(0, len(A)-1):
    B.append(float(sum(A)))
    A.pop(0)
B.append(float(sum(A)))
print(B)

# Cyclic shift

N = 3
k = 1000
seq = [9, 1, 2]

for i in range(1, k+1):
    x = seq.pop()

    seq.insert(0, x)

print(seq)