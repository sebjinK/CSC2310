import json

class Contact:
    def __init__(self, firstName: str, lastName: str, UID: int, dept: str, title: str, phone: str, building: str, POB: str)
        self.firstName = firstName
        self.lastName = lastName
        self.UID = UID
        self.email = firstName[0] + lastName + '@tntech.edu'
        self.dept = dept
        self.title = title
        self.building = building
        self.POB = POB


with open('contacts.json') as f:
    dataContacts = json.load(f)
    
for indexContacts in dataContacts:
    for key, value in indexContacts.items():
        print(key, ':', value)
    print('-' * 20)
print()
print()
    
# Read data from the JSON file
with open('events.json', 'r') as file:
    dataEvents = json.load(file)

# Iterate through the "university_events" list and print each event
for event in dataEvents['university_events']:
    print("Event ID:", event['UID'])
    print("Name:", event['Name'])
    print("Date:", event['Date'])
    print("StartTime:", event['StartTime'])
    print("Location:", event['Location'])
    print("Duration:", event['Duration'])
    print('-' * 20)
