# Dictionaries are HUGE

dictionary = {}
print(type(dictionary))

# dictionaries are { key, value } pairs
# username is a key, admin is the value
user = {
    "username": "admin",
    "password": "12345",
    "email": "test@gmail.com"
}

# print(user["username"])

multiples_users = [
    {
        "username": "admin",
        "password": "12345",
        "email": "test@gmail.com"
    },
    {
        "username": "AnotherUser",
        "password": "000000",
        "email": "t@gmail.com"
    }
]

print(type(multiples_users))   # prints list
print(type(multiples_users[0]))  # prints dict
print(multiples_users[0])  # gives entire user
print(multiples_users[0]["email"])  # gives users email
