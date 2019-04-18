from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

## led hardware ##
led_blue = LED(10)
led_red = LED(27)
led_green = LED(17)
## gui setup ##
win = Tk()
win.title(" LED Controller")
myFont = tkinter.font.Font(family = 'Helvetica',size = 12, weight = "bold")


## function ##
def led_blue_Toggle():
    if led_blue.is_lit:
        led_blue.off()
        ledBlueButton["text"] = "Turn Blue LED on"
    else:
        led_blue.on()
        ledBlueButton["text"] = "Turn Blue LED off"

def led_red_Toggle():
    if led_red.is_lit:
        led_red.off()
        ledRedButton["text"] = "Turn Red LED on"
    else:
        led_red.on()
        ledRedButton["text"] = "Turn Red LED off"

def led_green_Toggle():
    if led_green.is_lit:
        led_green.off()
        ledGreenButton["text"] = "Turn Green LED on"
    else:
        led_green.on()
        ledGreenButton["text"] = "Turn Green LED off"

def close():
    GPIO.cleanup()
    win.destroy()

### widgets ###
ledBlueButton = Button(win, text = "Turn Blue LED ON", font = myFont, command = led_blue_Toggle)
ledBlueButton.grid(row = 0, column = 1)
ledRedButton = Button(win, text = "Turn Red LED ON", font = myFont, command = led_red_Toggle)
ledRedButton.grid(row = 1, column = 1)
ledGreenButton = Button(win, text = "Turn Green LED ON", font = myFont, command = led_green_Toggle)
ledGreenButton.grid(row = 2, column = 1)

exitButton = Button(win, text = "Exit", font = myFont, command = close)
exitButton.grid( row = 3, column = 1)

win.protocol("WM_DELETE_WINDOW", close)