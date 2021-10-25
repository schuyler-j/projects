import time
import math
from math import pi
import re
import random
from PIL import Image
import sys

def main():

    #term colours
    OKBLUE = '\033[94m'
    OKRED = '\033[93m'
    OKGREEN = '\033[92m'
    OKBLACK = '\033[1m'

    COLOR_ONE = ''
    COLOR_TWO = ''



        #LEGACY
    #image = Image.open(fileImg)
    #wWidth, hHeight = image.size
    #print(hHeight, wWidth)

    #ratio = hHeight/wWidth
    #print(ratio)

    #nWidth = 100
    #nHeight = nWidth*ratio
    #nHeight = int (nHeight/1)
    #print(nWidth, nHeight)

    #size = (nWidth, nHeight)
    size = (120, 120)

    #time.sleep(0.2)
    fileImg = 'img.png'
    #fileImg = 'imgROT.png'
    image1 = Image.open(fileImg)

    f1 = image1.resize(size)
    f1.save("img.png")

    imgROT = 'imgROT.png'

    image1 = Image.open(imgROT)

    pix_access = image1.load()

    low  = "@"
    med  = ","
    high = " "
    low_med = "o"
    high_med = "*"

    payload = ""

    width, height = f1.size

    mul = 1

    #height
    ##width

    for x in range(width):
        for y in range(height):


            #list for rgb
            a = pix_access[x, y][0]
            b = pix_access[x, y][1]
            c = pix_access[x, y][2]

            a = a *mul 
            b = b *mul 
            c = c *mul 

            total = 765*mul
            #(80, 35, 65, 50)
            #(85, 65, 55, 45
            #(85, 70, 35, 20)
            #(80, 65, 45, 25)
            t = (total*0.70)
            hm =(total*0.60)
            m = (total*0.30)
            l = (total*0.20)

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
            with open("picture.txt", "a") as fileHop:
                fileHop.writelines(payload) 

            if chk > 0:
                payload = low
            else:
                payload = high
            #print(payload, end="")

                #COLOR MODE
            #if a%2==0:
            #    sys.stdout.write(f"{COLOR_ONE}"+payload)
            #    sys.stdout.flush()
            #else:
            #    sys.stdout.write(f"{COLOR_TWO}"+payload)
            #    sys.stdout.flush()

                #DEFAULT COLORS
            sys.stdout.write(f"{COLOR_ONE}"+payload)
            sys.stdout.flush()

        with open("picture.txt", "a") as fileHop:
            fileHop.writelines("\n")


def rotate():
    fImg = 'img.png'
    image = Image.open(fImg)
    
        #ROTATE
    angle = 90
    f0 = image.rotate(angle)
    f0.save("imgROT.png")



if __name__ == "__main__":

    rotate()

    while True:
        main()






