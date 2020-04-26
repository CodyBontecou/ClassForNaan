# What are the types of the following?:
# 1. "Hello" == string
# 2. ["Hello", 3] == list
# 3. { "Hello" : 3 } == dictonary
# 4. 3 == int
# 5. 6.7 == float
# 7. True == boolean
# 8. "False" == boolean
# Extra Credit: ("Hey", "Cutie") tupple with two strings

data = [
    {
       1: {"name": "Andrea", "age": "29", "nationality": "mexican"}
    },
    {
       1: {"name": "Cody", "age": "26", "nationality": "hawaiian"}

    },
    {
       1: {"name": "Daniela", "age": "23", "nationality": "mexican"}
    }
]

for n in data:
    #print(n) # n is data[0] in the first for loop
    print(n[1]["nationality"])


