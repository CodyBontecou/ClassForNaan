# Lesson 2: Lists
# ----------------------------


def header_text(text):
    print("-" * 50 + text + "-" * 50)


list = []
print(type(list))
print(len(list))

# Append adds to the end of a list
list.append("Hey")
print(len(list))
print(list)

# Multiple types within a list
list.append(1)
for item in list:
    print(type(item))

# Sorting the list
new_list = ["z", "a", "23", "hey"]
new_list.sort()
print(new_list)

# Reversed order of the list
new_list.reverse()
print(new_list)

header_text("nested for loops")
list_of_numbers = [1, 2, 10, 100]  # len = 4
multiplications = [1, 2, 5, 10]  # len = 4

# Because you're looping through both, you're looking at 16 (4 * 4)
for numbers in list_of_numbers:
    print("-" * 100)
    print(f'numbers: {numbers}')
    for numeros in multiplications:
        print(f'numeros: {numeros}')
        print(f'{numbers * numeros}')

third_list = [1, 0]
# The complixity here is now 4 * 4 * 2 = 32
for numbers in list_of_numbers:
    for numeros in multiplications:
        for number in third_list:
            print("ex")

# Big O of 4
for numbers in list_of_numbers:
    print("-" * 100)
    print(f'numbers: {numbers}')

# Also a Big O of 4
for numbers in multiplications:
    print("-" * 100)
    print(f'numbers: {numbers}')

print("-" * 100)
for i in range(len(list_of_numbers)):
    print(list_of_numbers[i] * multiplications[i])

header_text("list comprehension + zip example")
print([a * b for a, b in zip(list_of_numbers, multiplications)])


header_text("insert")
numbers = [1, 2, 3, 6, 7]
numbers.insert(3, 4)
print(numbers)
numbers.insert(4, 5)
print(numbers)

# HOMEWORK:
# Write a nested for loop that doesn't utilize the examples I showed or explained in class
