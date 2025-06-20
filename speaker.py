# it will speak

import pyttsx3

read = pyttsx3.init()

print("Type something :")
msg = input()

read.say(msg)

read.runAndWait()