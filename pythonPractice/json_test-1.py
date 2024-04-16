import json

with open('contacts.json') as f:
    data = json.load(f)

for x in data:
    for key, value in x.items():
        print(key, ':', value)
    print()
