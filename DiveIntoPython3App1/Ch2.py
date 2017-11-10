import os
import random
from random import randint


#os.

def print_everything(**kwargs):
    ''' example from stackoverflow'''
    for name, value in kwargs.items():
        print( '{0}. {1}'.format(name, value))
        

def yield_funNumber():
    ''' return a fun number. maybe random, maybe based on a pattern, whatever. '''
    while True:
        yield randint(1,10)

def table_things(**kwargs):
    for name, value in kwargs.items():
        print( '{0} = {1}'.format(name, value))

#print_everything('apple','banana','pear')

#for out in yield_funNumber():
#    print_everything(out)
#    input()

table_things(apple = 'fruit', cabbage = 'vegetable')
table_things(candle = 'mass', salad = [1,2,3])