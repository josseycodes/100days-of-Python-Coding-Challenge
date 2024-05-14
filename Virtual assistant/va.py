import speech_recognition as sr
import pyttsx3
import smtplib
import requests
from datetime import datetime, timedelta
import time
import threading

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"Recognized: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def send_email(to_email, subject, message):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "youremail@gmail.com"  # Replace with your email
        sender_password = "yourpassword"      # Replace with your password

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(sender_email, to_email, email_message)
        speak("Email has been sent successfully.")
    except Exception as e:
        speak(f"Failed to send email. Error: {str(e)}")

def get_weather(city):
    api_key = "your_openweather_api_key"  # Replace with your OpenWeather API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]['description']
        temp = main['temp']
        speak(f"The weather in {city} is currently {weather} with a temperature of {temp} degrees Celsius.")
    else:
        speak("City not found.")

def set_reminder(reminder_text, reminder_time):
    def reminder_thread(reminder_text, reminder_time):
        while True:
            if datetime.now() >= reminder_time:
                speak(f"Reminder: {reminder_text}")
                break
            time.sleep(1)
    thread = threading.Thread(target=reminder_thread, args=(reminder_text, reminder_time))
    thread.start()

def handle_command(command):
    if 'send email' in command:
        speak("To whom should I send the email?")
        to_email = listen()
        speak("What is the subject of the email?")
        subject = listen()
        speak("What should I say in the email?")
        message = listen()
        send_email(to_email, subject, message)
    elif 'weather' in command:
        speak("Which city's weather would you like to know?")
        city = listen()
        get_weather(city)
    elif 'set a reminder' in command:
        speak("What is the reminder?")
        reminder_text = listen()
        speak("When should I remind you? Please say the time in 24-hour format, for example, 15:30.")
        reminder_time_str = listen()
        try:
            reminder_time = datetime.strptime(reminder_time_str, "%H:%M").time()
            now = datetime.now()
            reminder_time = datetime.combine(now, reminder_time)
            if reminder_time < now:
                reminder_time += timedelta(days=1)
            set_reminder(reminder_text, reminder_time)
            speak(f"Reminder set for {reminder_time.strftime('%H:%M')}.")
        except ValueError:
            speak("I didn't understand the time format. Please try again.")
    else:
        speak("I'm sorry, I don't know how to do that yet.")

def main():
    speak("Hello, I am your virtual assistant. How can I help you today?")
    while True:
        command = listen()
        handle_command(command)

if __name__ == "__main__":
    main()
