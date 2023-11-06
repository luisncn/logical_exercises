"""
Remove repeated numbers from a list
"""

numbers = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 1, 2, 2, 2, 3, 3]

unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)
