import random

moy = 0;

i = 0

essai = 10000;

for i in range(essai):

    l = 1000000000

    i2 = 0;

    while l > 0:
        result = random.randrange(0, l, 1)
        i2 = i2 + 1
        l = result
        if(result == 0):    
            moy = moy + i2
            print("Tour :", i2)

    
    i = i +1

    print("Essai :", i)

print("Moyenne : ", moy/essai)
