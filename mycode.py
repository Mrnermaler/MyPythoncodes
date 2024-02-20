import pyttsx3
import webbrowser
import subprocess

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    # Asking for name
    name = input("Hello! What is your Name? ")
    speak(f"Hello {name}, nice to meet you")

    # Asking for a number
    number = int(input("Please enter a number: "))
    print("You entered:", number)

    # Asking for some text
    text_input = input("Please enter something: ")
    speak(text_input)
    print("You have entered:", text_input)

    # Opening a link
    link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(link)

    # If statement
    x = 150
    if x > 100:
        print("x is greater than 100")
    else:
        print("x is not greater than 100")

    # If-elif-else statement
    x = 10
    if x > 5:
        print("x is greater than 5")
    elif x == 5:
        print("x is equal to 5")
    else:
        print("x is less than 5")

    # Command execution
    command = "ls"  # Example command to list files in the current directory
    subprocess.run(command, shell=True)
