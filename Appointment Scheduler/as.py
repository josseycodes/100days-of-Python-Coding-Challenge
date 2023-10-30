import datetime

class Appointment:
    def __init__(self, date, time, purpose, location):
        self.date = date
        self.time = time
        self.purpose = purpose
        self.location = location

class AppointmentScheduler:
    def __init__(self):
        self.appointments = []

    def schedule_appointment(self, date, time, purpose, location):
        appointment = Appointment(date, time, purpose, location)
        self.appointments.append(appointment)
        print(f"Appointment scheduled for {date} at {time} for {purpose} at {location}.")

    def list_appointments(self):
        for idx, appointment in enumerate(self.appointments):
            print(f"Appointment {idx + 1}:")
            print(f"Date: {appointment.date}")
            print(f"Time: {appointment.time}")
            print(f"Purpose: {appointment.purpose}")
            print(f"Location: {appointment.location}")
            print()

    def check_availability(self, date, time):
        for appointment in self.appointments:
            if appointment.date == date and appointment.time == time:
                return False
        return True

# Main program
scheduler = AppointmentScheduler()

while True:
    print("Appointment Scheduler Menu:")
    print("1. Schedule an appointment")
    print("2. List all appointments")
    print("3. Check availability")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter the date (YYYY-MM-DD): ")
        time = input("Enter the time (HH:MM): ")
        purpose = input("Enter the purpose of the appointment: ")
        location = input("Enter the location: ")

        if scheduler.check_availability(date, time):
            scheduler.schedule_appointment(date, time, purpose, location)
        else:
            print("This time slot is already booked. Please choose another.")

    elif choice == "2":
        scheduler.list_appointments()

    elif choice == "3":
        date = input("Enter the date (YYYY-MM-DD): ")
        time = input("Enter the time (HH:MM): ")
        
        if scheduler.check_availability(date, time):
            print("The selected time slot is available.")
        else:
            print("The selected time slot is already booked.")

    elif choice == "4":
        print("Exiting the Appointment Scheduler. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
