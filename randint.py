#!/usr/bin/env python

#Function Returns a psudo random integer from 0 to 9 based of
#of previous guesses

from random import randint
start = raw_input("have you previously selected values? y/n: ")
flag = None
if start == 'y':
    flag = True
else:
    flag = False

if not flag:
    MAX = input("Largest ID previously selected: ")

    print("Last ID selection from 0 to 9: ")
    #---------------------------------
    #generates 2 psudo random integers
    #---------------------------------
    rand = randint(MAX,9) #or n in range(0,1)
    print(rand)
else:
    print(randint(0,9))

