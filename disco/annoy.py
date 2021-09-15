import random
from time import sleep
import win32
import keyboard
from win32 import win32clipboard
import io
from random import randint, shuffle
import re



search = ""


victim = input("Type the discord name of the individual you wish to annoy and hit Enter! : ")

    #keyboard.send("ctrl+v, enter")

j = []
a=1
while a == 1:
    #Gif picker
    print("hello")
    num = randint(0, 6)
    sleep(5) #give time to run away
    #with open('poc.txt', 'r') as file:
    #    data = file.readlines()
    with open('poc1.txt', 'r') as file:
        data = file.readlines()


    if num % 2 == 0:
        txt = data[num]
        x = re.findall("[a-z]{1}", txt)
        x = ''.join(x)
        print(x)
        x = re.findall("[a-z]{3}", x)

        b = randint(0, len(x)-1)
        print(x[b])
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(x[b])
        win32clipboard.CloseClipboard()

        keyboard.send("ctrl+g")
        sleep(0.5)
        keyboard.send("ctrl+v")
        sleep(2)
        keyboard.send("down")
        sleep(0.5)
        keyboard.send("enter")
    else:
        num = randint(0, 32)
        search = data[num]
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(victim)
        win32clipboard.CloseClipboard()

        keyboard.send("ctrl+v, space")

        sleep(1)

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(search)
        win32clipboard.CloseClipboard()

        keyboard.send("ctrl+v")
        keyboard.send("enter")

        sleep(0.5)



