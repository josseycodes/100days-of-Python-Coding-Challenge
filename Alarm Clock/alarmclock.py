import datetime
import winsound
import time

class Alarm:
    def __init__(self):
        self.alarms = {}

    def set_alarm(self, time_str, sound_file):
        alarm_time = datetime.datetime.strptime(time_str, "%H:%M")
        self.alarms[alarm_time] = sound_file

    def check_alarm(self):
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            for alarm_time, sound_file in self.alarms.items():
                if current_time == alarm_time.strftime("%H:%M"):
                    self.trigger_alarm(sound_file)
                    del self.alarms[alarm_time]
            time.sleep(60)  # Check every minute

    def trigger_alarm(self, sound_file):
        print("ALARM!")
        winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
        snooze = input("Enter 's' to snooze, any other key to stop the alarm: ")
        if snooze.lower() == 's':
            time.sleep(300)  # Snooze for 5 minutes (300 seconds)
            winsound.PlaySound(None, winsound.SND_PURGE)

def main():
    alarm_clock = Alarm()
    alarm_clock.set_alarm("07:00", "alarm.wav")  # Example alarm
    alarm_clock.check_alarm()

if __name__ == "__main__":
    main()
