import json

with open('states_titlecase.json') as f:
    data = json.load(f)
    
print(data)