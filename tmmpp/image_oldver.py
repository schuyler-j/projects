import math
from math import pi
import re
import random
from PIL import Image
import sys

def main():

    fileImg = 'img.png'

    image = Image.open(fileImg)

    size = (60, 60)

    pix_access = image.load()


    f0 = image.resize(size)
    f0.save("img.png")





    low  = "@"

    med  = ","

    high = "#"

    low_med = "o"

    high_med = "*"

    payload = ""

    width, height = f0.size

    mul = 1
    count = height

    for x in range(height):
        count = count - 1
        for y in range(width):



            a = pix_access[x, y][0]
            b = pix_access[x, y][1]
            c = pix_access[x, y][2]

            a = a *mul 
            b = b *mul 
            c = c *mul 

            total = 765*mul
            t = (total*0.80)
            l = (total*0.25)

            chk = total-(a+b+c)

            hm = (total*0.75)
            m = (total*0.40)


            if chk >= t:
                payload = high
            elif chk < hm and chk > m:
                payload = med
            elif chk < l:
                payload = low
            elif chk < t and chk > hm:
                payload = high_med
            elif chk < m and chk > l:
                payload = low_med
            with open("picture.txt", "a") as fileHop:
                fileHop.writelines(payload) 

            #print(payload, end="")

            sys.stdout.write(payload)
            sys.stdout.flush()







if __name__ == "__main__":
    while True:
        main()






