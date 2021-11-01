import time
import math
from math import pi
import re
import random
from PIL import Image
import sys

def main():



    size = (120, 120)


    low  = "@"
    med  = ","
    high = "-"
    low_med = "o"
    high_med = "*"

    payload = ""

    width, height = size

    mul = 1
    count = 0

    #height
    ##width

    for x in range(width):
        for y in range(height):
            count = count + 1


            #list for rgb
            a = random.randint(0, 155)
            b = random.randint(100, 255)
            c = random.randint(50, 255)

            a = a *mul 
            b = b *mul 
            c = c *mul 
            c=math.sin(count)*a

            total = 765*mul
            #(80, 35, 65, 50)
            #(85, 65, 55, 45
            #(85, 70, 35, 20)
            #(80, 65, 45, 25)
            t = (total*0.95)
            hm =(total*0.85)
            m = (total*0.35)
            l = (total*0.25)



            chk = total-(a+b+c)

            #calculate brightness
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

            #print(payload, end="")

            sys.stdout.write(payload)
            sys.stdout.flush()



if __name__ == "__main__":

    while True:
        main()
