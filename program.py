import tkinter as tk
import RPi.GPIO as GPIO
import time

#LED Connection Details
LED_PIN = 15
LED_ON = True
LED_OFF = False

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Morse code dictionary
MORSE_CODE = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " ": "_",
}

def blink_led(morse_code):
    for dot_or_dash in morse_code:
        if dot_or_dash == ".":
            time.sleep(0.25)
            GPIO.output(LED_PIN, LED_ON)
            time.sleep(0.25)
            GPIO.output(LED_PIN, LED_OFF)
        elif dot_or_dash == "-" :
            time.sleep(0.75)
            GPIO.output(LED_PIN, LED_ON)
            time.sleep(0.75)
            GPIO.output(LED_PIN, LED_OFF)

def word_array(word):
    for i in word:
        if(len(word) <= 12):
            blink_led(MORSE_CODE[i])
            print(i)
        else:
            print("Sorry Maximum of 12 characters are allowed")
            return;

def on_button_click():
    word = text_box.get()
    word_array(word.lower())
    
def close():
    GPIO.cleanup()
    root.destroy()

root = tk.Tk()

# Set window title
root.title("Morse Code LED Blinker")

# Create a text box
text_box = tk.Entry(root)
text_box.pack()

# Create a button
button = tk.Button(root, text="Blink", command=on_button_click)
button.pack()

root.protocol('WM_DELETE_WINDOW', close)

# Start the main loop
root.mainloop()