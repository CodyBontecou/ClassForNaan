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
        2: {"name": "Cody", "age": "26", "nationality": "hawaiian"}

    },
    {
        3: {"name": "Daniela", "age": "23", "nationality": "mexican"}
    }
]

for person in data:
    for key, value in person.items():
        print(value["nationality"])

users = [
    {
        "name": "Daniela",
        "age": 23,
        "height": 157,
        "nicknames": {
            1: "Naan",
            2: "Lovebug",
            3: "Dani"
        }
    },
    {
        "name": "Cody",
        "age": 26,
        "height": 170,
        "nicknames": {
            1: "Lovebug",
            2: "Codyman",
            3: "Hawaii"
        }
    }
]

# for user in users:
#     print(user["nicknames"].items())
#     for key, value in user["nicknames"].items():
#         print(key, value)

# print(users[1])
