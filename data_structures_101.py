# Data Structures 101 in Python

example_break = "*"*100

# Primitive types
string = "variable example"
int = 1
float = 2.4
boolean = True

# Data structures
list = []
dictionary = {}
tuple = ()

# String slicing
phone_number = "970-275-4211"
area_code = phone_number[:3]
print(area_code)
last_four_digits = phone_number[8:]  # [8:] is the same as [8:len(phone_number)]
print(last_four_digits)
middle_three_digits = phone_number[4:7]  # Actually only looking at indexes 4, 5, and 6
print(middle_three_digits)
print(phone_number[:-5])  # prints 970-275
print(phone_number[-4:])  # prints 4211
print(phone_number[-8:-5])  # prints 275. Same as middle_three_digits logic

sentence = "Hey Daniela"
sentence += ", how are you?"  # S
print(sentence)
hey = sentence[:3]
rest = sentence[11:]
sliced_sentence = hey + rest
print(sliced_sentence)
replaced_sentence = sentence.replace(" Daniela", "")
print(replaced_sentence)

# String concatenation
sentence = "Hey Daniela"
sentence += ", how are you?"  # Same as sentence = sentence + ", how are you?"
print(sentence)

print(example_break)

double_quotes = "Daniela said \"what a beautiful morning\". "
print(double_quotes)

print(example_break)

single_quotes = 'Daniela said "what a beautiful morning".'
print(single_quotes)

print(example_break)

newline = "Daniela said \"what a beautiful morning\".\nCody replied \"Why yes Dani, it really is!\""
print(newline)

print(example_break)

danielas_line = "Daniela said \"What a beautiful morning\". "
codys_reply = "Cody replied \"Why yes Dani, it really is!\""
f_string = f"{danielas_line}\n{codys_reply}"
print(f_string)

print(example_break)

# Old way of doing this
name = "Eric"
print("Hello, %s." % name)

print(example_break)

names = ["Beta", "Dani", "Rocio", "Cody", "Ro"]
for name in names:
    print(f"Hi {name}!")
