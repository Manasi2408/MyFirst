# you can type whatever you want and it will speak what u have typed

import pyttsx3

read = pyttsx3.init()

print("Type something :")
msg = input()

read.say(msg)

read.runAndWait()