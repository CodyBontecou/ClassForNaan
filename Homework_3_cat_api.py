import requests

break_thing = ("*" * 100)

for i in range(5):
    cat_data = requests.get("https://cat-fact.herokuapp.com/facts/random").json()
    print(cat_data["text"])

print(break_thing)

facts_two = requests.get("https://cat-fact.herokuapp.com/facts?animal_type=horse").json()
for horse in facts_two["all"]:
    if "name" in
    print(horse["user"]["name"])
    break

"""
{
    u'text': u"If a horse's ears are pointing in different directions, the horse is looking at two different things at the same time.",
    u'userUpvoted': None, u'upvotes': 1, u'_id': u'5b7a07a32048fd0014e9d8b2', u'type': u'horse',
    u'user': {u'_id': u'5a9ac18c7478810ea6c06381', u'name': {u'last': u'Wohlbruck', u'first': u'Alex'}}
    }
"""