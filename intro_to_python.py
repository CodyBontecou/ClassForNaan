import requests

r = requests.get('https://api.github.com/user', auth=('bontecouc@gmail.com', 'Hhtpqrs1234'))
print(r)
