import json

# Load contacts and events from JSON files
with open('contacts.json') as contacts_json:
    contacts = json.load(contacts_json)

with open('events.json') as events_json:
    events_data = json.load(events_json)
    events = events_data['university_events']

# Define Contact and Event classes
class Contact:
    def __init__(self, data):
        self.first_name = data['FirstName']
        self.last_name = data['LastName']
        self.uid = data['UID']
        self.email = data['EmailAddress']
        self.department = data['Dept']
        self.title = data['Title']
        self.phone = data['Phone']
        self.building = data['Building']
        self.po_box = data['POBox']
        self.last_communication_date = None

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"User ID: {self.uid}")
        print(f"Email: {self.email}")
        print(f"Department: {self.department}")
        print(f"Title: {self.title}")
        print(f"Phone: {self.phone}")
        print(f"Building: {self.building}")
        print(f"PO Box: {self.po_box}")
        if self.last_communication_date:
            print(f"Last Communication Date: {self.last_communication_date}")
        print("\n")

class Event:
    def __init__(self, data):
        self.name = data['Name']
        self.uid = data['UID']
        self.date = data['Date']
        self.start_time = data['StartTime']
        self.location = data['Location']
        self.duration = data['Duration']
        self.actionItems = []
        self.numActionItems = 0

    def display_info(self):
        print()
        print(f"Event Name: {self.name}")
        print(f"Event ID: {self.uid}")
        print(f"Date: {self.date}")
        print(f"Start Time: {self.start_time}")
        print(f"Location: {self.location}")
        print(f"Duration: {self.duration} hours")
        if self.numActionItems > 0:
            print(f"Action items associated with {self.name}: {', '.join(self.action_items)}\n")
        print()

# Create Contact and Event objects
contacts_objects = [Contact(singleContact) for singleContact in contacts]
events_objects = [Event(singleEvent) for singleEvent in events]

# User interaction loop
while True:
    print("Choose an option:")
    print("1. View list of contacts")
    print("2. View list of events")
    print("3. Input last date of communication for a contact")
    print("4. Associate action items with an event")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        for contact_obj in contacts_objects:
            contact_obj.display_info()

    elif choice == '2':
        for event_obj in events_objects:
            event_obj.display_info()

    elif choice == '3':
        uid = int(input("Enter the UID of the contact: "))
        for contact_obj in contacts_objects:
            if contact_obj.uid == uid:
                last_comm_date = input("Enter the last communication date (YYYY-MM-DD): ")
                contact_obj.last_communication_date = last_comm_date
                print(f"Last communication date for {contact_obj.first_name} {contact_obj.last_name} updated.\n")
                break
        else:
            print("Contact not found.\n")

    elif choice == '4':
        uid = int(input("Enter the UID of the event: "))
        for event_obj in events_objects:
            if event_obj.uid == uid:
                numActionItems = int(input('How many action items do you want to input? '))
                event_obj.action_items = []  # Reset the action items list for the event
                event_obj.numActionItems = numActionItems

                for i in range(numActionItems):
                    action_item = input("Enter action item: ")
                    event_obj.action_items.append(action_item)

                print(f"Action items associated with {event_obj.name}: {', '.join(event_obj.action_items)}\n")
                break
        else:
            print("Event not found.\n")

    elif choice == '5':
        print("Exit event planner")
        break

    else:
        print("Invalid choice. Please try again.\n")
