# Boolean -- True/False

break_thing = "*" * 100

# One `=` sets something equal
# For example: name = "Cody".
# Name is now the same as "Cody"

# Two `==` is checking if the statement is True.
# For example: name == "Cody" would be the same
# as True.
# BUT: name == "Daniela" would be the same as False.
name = "Cody"
if name == "Cody":
    print("Hey, it's Cody")
else:
    print("Nope, not Cody")

print(name == "Cody")
print(name == "Daniela")

print(break_thing)

list_of_names = ["Cody", "Daniela"]
for i in range(len(list_of_names)):
    print(i)

print(break_thing)

print(len(list_of_names) == 2)

print(break_thing)

# This will only print Cody and Daniela
list_of_new_names = ["Cody", "Daniela", "Rocio"]
for i in range(2):
    print(list_of_new_names[i])

print(break_thing)

print(len(list_of_new_names))

print(break_thing)

wedding_list = [
    {
        "name": "Daniela",
        "menu": "Vegetarian"
    },
    {
        "name": "Cody",
        "menu": "Vegan"
    },
    {
        "name": "Rocio",
        "menu": "Normal"
    },
    {
        "name": "Andrea",
        "menu": "Normal"
    },
    {
        "name": "Beto",
        "menu": "Normal"
    },
    {
        "name": "Sergio",
        "menu": "Vegan"
    }
]

# Check all invites and see get a count of each menu type.
for guest in wedding_list:
    # if "Vegetarian" == "Vegetarian"
    if "Vegetarian" in guest["menu"]:  # guest["menu"] == "Vegetarian" or "Vegan" or "Normal" depending on the guest
        print(guest["menu"])

print(break_thing)

# Print the number of Normal menus with counter method

counter = 0
# For every guest
for guest in wedding_list:
    # if that guests menu is normal
    if guest["menu"] == "Normal":
        counter += 1
        # then print that guest
        print(guest)
print(counter)

print(break_thing)
# Print the number of Normal menus with count() function
guests_with_normal_menu = []
for guest in wedding_list:
    if guest["menu"] == "Normal":
        # == to guests_with_normal_menu = [guest, ...].
        # Append adds a guest to the new list after each iteration of the loop
        guests_with_normal_menu.append(guest)
print(len(guests_with_normal_menu))
print(guests_with_normal_menu)

# [ guest, guest guest, guest, guest guest ] current wedding list
# [ { normals: [guest, guest, guest] }, { vegans: [guest, guest] }, { vegetarian: [guest] } ]

print(break_thing)

sorted_menus = []
for guest in wedding_list:
    if guest["menu"] not in sorted_menus:
        sorted_menus.append(guest["menu"])
# for menu in sorted_menus:
#     if guest["menu"] == menu:
#         menu
print(sorted_menus)
