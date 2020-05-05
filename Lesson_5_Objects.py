# Objects
# An object is a different form of structuring your data
# Objects are the main point of Object Oriented Programming (OOP)

# Function declaration
# def animal():


class Animal:  # Object declaration
    def __init__(self, name, color):
        self.name = name
        self.color = color


sandy = Animal(name="Sandy", color="blonde")

print(sandy)  # <__main__.Animal object at 0x106b5b278>
print(type(sandy))  # <class '__main__.Animal'>
print(type("hello"))  # <class 'str'>
print(sandy.name)  # Sandy


class Guest:
    def __init__(self, name, menu="Normal"):
        self.name = name
        self.menu = menu
        self.poop_color = "brown"

    def lowercase_name(self):
        return self.name.lower()


guest_list = [
    Guest(name="Beto", menu="Vegetarian"),
    Guest(name="Daniela", menu="Normal"),
    Guest(name="Cody", menu="Vegan")
]

for guest in guest_list:
    print(guest.menu)

# Inheritance


