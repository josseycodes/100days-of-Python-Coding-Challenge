import time
import datetime
import threading

class Event:
    def __init__(self, name, date_time, reminder_times):
        self.name = name
        self.date_time = date_time
        self.reminder_times = reminder_times

class EventCountdownTimer:
    def __init__(self):
        self.events = []

    def add_event(self, name, date_time_str, reminder_times):
        date_time = datetime.datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
        new_event = Event(name, date_time, reminder_times)
        self.events.append(new_event)
        print(f"Event '{name}' added successfully!")

    def start(self):
        print("Starting the event countdown timer...")
        while True:
            current_time = datetime.datetime.now()
            for event in self.events:
                self.check_reminders(event, current_time)
            time.sleep(60)  # Check every minute

    def check_reminders(self, event, current_time):
        time_left = event.date_time - current_time
        if time_left.total_seconds() <= 0:
            print(f"Event '{event.name}' is happening now!")
            self.events.remove(event)
        else:
            for reminder in event.reminder_times:
                reminder_time = event.date_time - datetime.timedelta(minutes=reminder)
                if current_time >= reminder_time:
                    print(f"Reminder: Event '{event.name}' is happening in {reminder} minutes.")
                    event.reminder_times.remove(reminder)

def main():
    timer = EventCountdownTimer()

    def add_event_thread():
        while True:
            name = input("Enter the event name: ")
            date_time_str = input("Enter the event date and time (YYYY-MM-DD HH:MM:SS): ")
            reminder_times = input("Enter reminder times in minutes before the event (comma-separated): ")
            reminder_times = [int(x) for x in reminder_times.split(",")]
            timer.add_event(name, date_time_str, reminder_times)

    event_thread = threading.Thread(target=add_event_thread)
    event_thread.start()

    timer.start()

if __name__ == "__main__":
    main()
