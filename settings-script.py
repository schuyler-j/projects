import io
import time
from random import shuffle, randint, choice
#how does python work again???

#i'll append because i don't wanna use regex atm...


true = 1
while true == 1:
    with open('settings.json', 'r') as file:
        data = file.readlines()

    a = choice([(48, 57), (65, 70)])
    a = randint(*a)
    b = choice([(48, 57), (65, 70)])
    b = randint(*b)
    c = choice([(48, 57), (65, 70)])
    c = randint(*c)

    d = choice([(48, 57), (65, 70)])
    d = randint(*d)
    e = choice([(48, 57), (65, 70)])
    e = randint(*e)
    f = choice([(48, 57), (65, 70)])
    f = randint(*f)

    new_hex = ["#", chr(a), chr(b), chr(c), chr(d),chr(e), chr(f)]

    z = ''.join(new_hex)

    #take a rest
    time.sleep(0.9)

    newString = '"foreground": "' + z + '",'

    guess = randint(97, 104)
    data[guess] = '            ' + newString + '\n'


    with open('settings.json', 'w') as file:
        file.writelines(data)



