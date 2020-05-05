# Iterables allow you to iterate through data
# From my knowledge, there are two main iterables
# For loops, and while loops.

# Just a quick overview of for loops. You already know these very well.

for i in range(10):
    print(i)

users = [{"name": "Cody", "age": 26}, {"name": "Daniela", "age": 23}]
for user in users:
    print(user["name"])

# A while loop follows the following structure:
# while True:
    # do something

number = 10
while number > 0:
    print(number)
    if number == 5:
        print("It's 5")
    number -= 1

# from time import gmtime, strftime, time
#
# while int(strftime("%Y-%m-%d %H:%M:%S", gmtime()[:4])) <= 2020:
#     print("Hey Dany")
#     time.sleep(10)
#     print("It's still not 2021")
