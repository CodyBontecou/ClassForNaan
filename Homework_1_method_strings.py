# Method Strings Homework 1

# String
break_thing = "*"*100

#Slicing() eturn a range of characters by using the slice syntax.

sentence = "Hello, how are you? my name is Daniela and yours?"
print(sentence[0:5])
print(sentence[20:])

print(break_thing)

#len() get the length of a string

names = ["Rodrigo", "Daniela", "Cody", "Bernardo"]
if names[0] == "Rodrigo":
    print(len(names[2]))
else:
    print("error")

print(break_thing)

#sort

data = ["17809", "20203", "14590", "167777", "29402"]

def sort_postal_codes(codes):
    for number in codes:
         if number[0] == "1":
            print(number)

sort_postal_codes(data)

print(break_thing)

#lower and upper() returns the string in lower/upper case.

a = "ME LLAMO"
b = "daniela"
print(f"{a.lower()},{b.upper()}")

print(break_thing)

#strip() removes any whitespace from the beginning or the end.

a = "           I think Cody is very cute            "
print(a.strip())

print(break_thing)

#replace() eplaces a string with another string.

fruits_with_a = "Opple, Opricot"
fruits_with_b = "Eanana, Elueberries"
print(fruits_with_a.replace("O", "A"))
print(fruits_with_b.replace("E", "B"))

print(break_thing)

#split() returns a list of strings after breaking the given string by the specified separator.

phrase = "Like, Apples?"
print (phrase.split(","))

print(break_thing)

#capitalize() converts the first character of a string to uppercase letter.

name = "daniela"
last_name = "gonzalez"
second_last_name = "barron"
print(name.capitalize() + " " + last_name.capitalize() + " " + second_last_name.capitalize())

print(break_thing)

#count()  returns count of how many times a given object occurs in list.

kitchen_items = ["Eggs", "Coffee", "Milk", "Soy", "Ham", "Rice", "Spinach", "Coffee", "Cereal", "Coffee", "Cereal", "Coffee", "Cereal"]
print(kitchen_items.count("Coffee"))

print(break_thing)

#title() used to convert the first character in each word to Uppercase.

str1 = " and the chamber of secrets"
str2 = str1.title()
print(f"Harry Potter{str2}")

print(break_thing)

#rfind() returns the highest index of the substring.

name1 = "DanielaGonzalezBarron"
result1 = name1.rfind("lez")
result2 = name1.rfind("Gon")
result3 = name1.rfind("rron")
result4 = name1.rfind("Dan")
print(result1)
print(result2)
print(result3)
print(result4)

print(break_thing)

#islower() checks if all characters in the string are lowercase.

a = "hello me llamo daniela"
b = "Hello me llamo Daniela"
print(a.islower())
print(b.islower())

print(break_thing)

#index() searches for given element from start of the list and returns the lowest index where the element appears.

list1 = ["b", "a", "c", "d", "e", "f", "a", "a", "c"]
print(list1.index("a"))

print(break_thing)

#find()  returns the lowest index of the substring if it is found in given string. If its is not found then it returns -1.

phrase = "today is not monday"
print(phrase.find("not"))

print(break_thing)

#endswith() returns True if a string ends with the given suffix otherwise returns False.

text1 = "Cuantos cuentos cuentas"
text2 = "Cuando cuentas cuentos"
text3 = "Nunca cuentas cuantos cuentos cuentas"
result = text1.endswith("cuentas")
print(result)
result = text2.endswith("cuentas")
print(result)
result = text3.endswith("cuentas")
print(result)
