#!/usr/bin/env python

#Function Returns a psudo random integer from 0 to 9 based of
#of previous guesses

from random import randint
import operator

start = raw_input("have you previously selected values? y/n: ")
flag = None
if start == 'y':
    flag = True
else:
    flag = False

if  flag:
    MAX = input("How Many ID's previously selected: ")
    print MAX
    values = [0 for x in range(9)]
    i = 0
    while i < MAX:
        values[i] = input("Last ID selection from 0 to 9: ")
        i = i + 1

    #---------------------------------
    #generates psudo random integers
    #---------------------------------
    rand = randint(0,9) #or n in range(0,1)
    print "\n"
    #print values
    j = 0
    while j < MAX:
        #print values[j]
        if values[j] == rand:
            rand = randint(0,(values[j]-1))+randint((values[j]+1),9)
            j = j + 1
        else:
            j = j + 1

    print rand;

if not flag:
    #MAX = input("Largest ID previously selected: ")

    print("Last ID selection from 0 to 9: ")
    #---------------------------------
    #generates 2 psudo random integers
    #---------------------------------
    rand = randint(0,9) #or n in range(0,1)
    print(rand)
