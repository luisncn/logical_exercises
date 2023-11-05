"""
Remove repeated numbers from a list
"""

numbers = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 9]
numbers_repeated = []

for number in numbers:
    check = number in numbers_repeated
    if number == check:
        continue
    else:
        del numbers[number]

print(numbers)
