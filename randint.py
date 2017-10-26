#!/usr/bin/env python

#Function Returns a psudo random integer from 0 to 9 based of
#of previous guesses

from random import randint
<<<<<<< HEAD
import operator
=======
>>>>>>> 2cc386eda9b6f1b8ea7e4b96a851ce551ad78607
start = raw_input("have you previously selected values? y/n: ")
flag = None
if start == 'y':
    flag = True
else:
    flag = False

<<<<<<< HEAD
if  flag:
    MAX = input("How Many ID's previously selected: ")
    values = [0 for x in range(9)]
    print (values)
    print(operator.itemgetter(0)(values))
    i = 0
    while i < MAX:
        values = input("Last ID selection from 0 to 9: ")
        i = i + 1

    #---------------------------------
    #generates psudo random integers
    #---------------------------------
    rand = randint(0,9) #or n in range(0,1)
    j = 0
    while j < MAX:
        k = operator.itemgetter(0)(values)
        print(j)
        print(k)
        if values == rand:
            rand = randint(0,9)
            j = j + 1
        else:
            j = j + 1
=======
if not flag:
    MAX = input("Largest ID previously selected: ")

    print("Last ID selection from 0 to 9: ")
    #---------------------------------
    #generates 2 psudo random integers
    #---------------------------------
    rand = randint(MAX,9) #or n in range(0,1)
>>>>>>> 2cc386eda9b6f1b8ea7e4b96a851ce551ad78607
    print(rand)
else:
    print(randint(0,9))

