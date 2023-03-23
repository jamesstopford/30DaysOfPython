# main.py file
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh


from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3


import math as m
print(m.pi)           # 3.141592653589793, pi constant
print(m.sqrt(2))      # 1.4142135623730951, square root
print(m.pow(2, 3))    # 8.0, exponential function
print(m.floor(9.81))  # 9, rounding to the lowest
print(m.ceil(9.81))   # 10, rounding to the highest
print(m.log10(100))   # 2, logarithm with 10 as base


from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive