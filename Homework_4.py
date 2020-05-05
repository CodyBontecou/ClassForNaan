# 120% -- Good work!

import requests

break_thing = "*"*200

dog_data = requests.get("https://api.thedogapi.com/v1/breeds?attach_breed=0").json()
for i in dog_data:
    if "bred_for" in i:
        print(i["bred_for"])

print(break_thing)

for dog in dog_data:
    if "country_code" in dog:
        if "US" in dog["country_code"]:
            print(dog["bred_for"])


{u'origin': u'Germany, France', u'name': u'Affenpinscher', u'weight':
    {u'metric': u'3 - 6', u'imperial': u'6 - 13'},
 u'bred_for': u'Small rodent hunting, lapdog', u'life_span': u'10 - 12 years',
 u'height':
     {u'metric': u'23 - 29', u'imperial': u'9 - 11.5'},
 u'temperament': u'Stubborn, Curious, Playful, Adventurous, Active, Fun-loving', u'breed_group': u'Toy', u'id': 1}

