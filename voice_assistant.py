import speech_recognition as sr 
import pyttsx3
import pywhatkit
import wikipedia
import datetime 
import sys  

r = sr.Recognizer()
phone_numbers = {"ritu": "2347859493", "rohini": "5285949328", "vaishnavi": "9023478524"}
bank_account_numbers = {"an": "358449591", "wt": "195844953"}

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('Listening... Ask now...')
            audioin = r.listen(source)
            my_text = r.recognize_google(audioin)
            my_text = my_text.lower().strip()  
            print(my_text)
            
            # Greetings
            if 'hi' in my_text or 'hello' in my_text:
                speak("Hello! How can I assist you?")

            elif 'how are you' in my_text or 'how are you doing' in my_text:
                speak("I'm doing great! Thanks for asking. How can I help you?")

            # Answer "What do you do?"
            elif 'what do you do' in my_text:
                speak("I can play music, tell you the time and date, provide information from Wikipedia, fetch phone numbers, and more! Just ask.")

            # Answer "What is your name?"
            elif 'what is your name' in my_text:
                speak("I am your virtual assistant.")

            # Ask to play
            elif 'play' in my_text:
                song = my_text.replace('play', '').strip()
                speak('Playing ' + song)
                pywhatkit.playonyt(song)

            # Ask for date
            elif 'date' in my_text:
                today = datetime.date.today().strftime('%B %d, %Y')
                speak("Today's date is " + today)

            # Ask for time
            elif 'time' in my_text:
                timenow = datetime.datetime.now().strftime('%H:%M')
                speak("The current time is " + timenow)

            # Ask details about any person
            elif "who is" in my_text:
                person = my_text.replace('who is', '').strip()
                info = wikipedia.summary(person, 1)
                speak(info)

            # Ask phone numbers
            elif "phone number" in my_text:
                for name in phone_numbers:
                    if name in my_text:
                        speak(f"{name}'s phone number is {phone_numbers[name]}")
                        break

            # Ask personal bank account numbers
            elif "account number" in my_text:
                for bank in bank_account_numbers:
                    if bank in my_text:
                        speak(f"{bank}'s bank account number is {bank_account_numbers[bank]}")
                        break

            # Ask for "Thank you" response 
            elif 'thank you' in my_text or 'thanks' in my_text or 'thank' in my_text:
                speak("You're welcome! Always happy to help.")

            # Exit when user says "bye" 
            elif 'bye' in my_text or 'goodbye' in my_text:
                speak("Goodbye! Have a great day.")
                sys.exit()

            # If not recognized
            else:
                speak("Please ask a correct question.")

    except Exception as e:
        print('Error:', e)  

while True:
    commands()



