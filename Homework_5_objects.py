# class Test:
# def fun(self): #def = function
# print("Hello")

# obj = Test()
# obj.fun()

break_thing = "*" * 100

List = ["daniela", "cody is great", "rocio", "cody lovebug", "beto", "cody Bontecou"]
data = ["apple", "banana", "cody"]


def my_first_function(list):
    for name in list:
        if "cody" in name:
            print(name)


my_first_function(List)
my_first_function(data)
# two blank lines

print(break_thing)


# Class

class cody:
    def __init__(object, name, age):
        object.name = name
        object.age = age


    def myfunc(self):
        print("hello my name is " + self.name + ", my age is " + str(self.age))



p1 = cody("Cody Bontecou", 26)
p1.myfunc()
#Methods in objects are functions that belong to the object.