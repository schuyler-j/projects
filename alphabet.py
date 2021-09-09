

word = input("Word to encrypt? ") 
#passes = int(input("How many passes? "))
word = word.upper()

alphabet = {
    "A":10025,
    "B":10124,
    "C":10223,
    "D":10322,
    "E":10421,
    "F":10520,
    "G":10619,
    "H":10718,
    "I":10817,
    "J":10916,
    "K":11015,
    "L":11114,
    "M":11213,
    "N":11312,
    "O":11411,
    "P":11510,
    "Q":11609,
    "R":11708,
    "S":11807,
    "T":11906,
    "U":12005,
    "V":12104,
    "W":12203,
    "X":12302,
    "Y":12401,
    "Z":12500,
}

alphabet_ref = {
    '10025':"A",
    '10124':"B",
    '10223':"C",
    '10322':"D",
    '10421':"E",
    '10520':"F",
    '10619':"G",
    '10718':"H",
    '10817':"I",
    '10916':"J",
    '11015':"K",
    '11114':"L",
    '11213':"M",
    '11312':"N",
    '11411':"O",
    '11510':"P",
    '11609':"Q",
    '11708':"R",
    '11807':"S",
    '11906':"T",
    '12005':"U",
    '12104':"V",
    '12203':"W",
    '12302':"X",
    '12401':"Y",
    '12500':"Z",
}

keys = list(alphabet)

neighbour = []
j = [] 


k = 99 #constant displacement
count = 0
flip = 0 
passes = 5


word = word.split() 



for i in word:
    c = word[count]
    count = count + 1
    for b in c:
        #nextL = alphabet[word[count+1]]
        #nextL = nextL % 100
        #print(nextL)

        i = alphabet[b]
        a = i % 100

        
        if i > 10900:
        
            i = i % 10000
        
        else:
        
            i = i % 1000 
        
        i = i // 100



        #i = i + passes

        #passes = a - nextL


        for x in range(len(word)):

            i = i + passes
            if i > 12:
                i = i - passes - x
            else:
                i = i + passes + x
            j.append(i)

        #if flip == 1:
        #    meal =6*k + passes*k
        #else:
        #    meal = 6*k
        #i = i + meal 

        #j.append(i)


        #flip = 1


        i = keys[i]
        print(i)
    
for r in range(len(j)):
    if j[r] < 10:
        j[r] = str("10") + str(j[r]) + str(25-j[r])
    elif 25-j[r] < 10:
        j[r] = str("1") + str(j[r]) + str("0") +str(25-j[r])
    else:
        j[r] = str("1") + str(j[r]) + str(25-j[r])

for r in j:
    print(alphabet_ref[r], end="")
#space
print("")

print(j)
#cast all to str
for z in range(len(j)):
    j[z] = str(j[z])

z = ''.join(j)
print(z)
