import datetime

class Event:
    def __init__(self, name, date_time):
        self.name = name
        self.date_time = date_time
        self.guests = []

    def add_guest(self, guest):
        self.guests.append(guest)

    def display_details(self):
        print(f"Event: {self.name}")
        print(f"Date and Time: {self.date_time}")
        print("Guests:")
        for guest in self.guests:
            print(f"  - {guest}")

class Guest:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"


class EventPlanner:
    def __init__(self):
        self.events = []

    def create_event(self, name, date_time):
        event = Event(name, date_time)
        self.events.append(event)
        return event

    def find_event(self, name):
        for event in self.events:
            if event.name == name:
                return event
        return None

    def display_events(self):
        if not self.events:
            print("No events found.")
            return
        print("Events:")
        for event in self.events:
            print(f"- {event.name}")

if __name__ == "__main__":
    planner = EventPlanner()

    while True:
        print("\nEvent Planner Menu:")
        print("1. Create Event")
        print("2. View Events")
        print("3. Add Guest to Event")
        print("4. Display Event Details")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            event_name = input("Enter event name: ")
            date_str = input("Enter event date and time (YYYY-MM-DD HH:MM): ")
            date_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            planner.create_event(event_name, date_time)
            print(f"Event '{event_name}' created successfully.")

        elif choice == "2":
            planner.display_events()

        elif choice == "3":
            event_name = input("Enter event name: ")
            event = planner.find_event(event_name)
            if event:
                guest_name = input("Enter guest name: ")
                guest_email = input("Enter guest email: ")
                guest = Guest(guest_name, guest_email)
                event.add_guest(guest)
                print(f"Guest '{guest_name}' added to '{event_name}'.")
            else:
                print(f"Event '{event_name}' not found.")

        elif choice == "4":
            event_name = input("Enter event name: ")
            event = planner.find_event(event_name)
            if event:
                event.display_details()
            else:
                print(f"Event '{event_name}' not found.")

        elif choice == "5":
            print("Exiting Event Planner. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
    