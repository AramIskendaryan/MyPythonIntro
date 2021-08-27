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

# new_number = input()
# value = "Boring"
# y = len(new_number)
#
# if len(new_number) != 1:
#     first = new_number[0]
#     for i in new_number[1:y-1]:
#         if i != first:
#             value = "interesting"
#             break
# print(value)

# Largest Number
# version 1

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


