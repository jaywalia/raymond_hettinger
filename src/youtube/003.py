# https://www.youtube.com/watch?v=HTLu2DFOdTg&list=PLRVdut2KPAguz3xcd22i_o_onnmDKj3MA&index=3

# classes

import math

'''
Circuitious, LLC -
An advanced Circle Analytics Company

'''

#===============================================================================
# always inherit from object
class Circle(object):
    'An advanced circle analytics company'

    version = '0.1'

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius**2 * math.pi





#===============================================================================
def selfTest():
    print('selfTest')
    print(f'Circuitious, LLC - {Circle.version}')
    c = Circle(2)
    print(f'Circle with radius:{c.radius} has area: {c.area():.2f}')

#===============================================================================
def academiaTest():
    from random import random, seed
    seed(202205280412) 
    print('academiaTest')
    n = 10
    circles = [Circle(random()) for i in range(n)]
    print(f'{n} circles created')
    avg_area = sum([c.area() for c in circles]) / n
    print(f'The average area of {n} circles is {avg_area:.2f}')
#===============================================================================
def main():
    selfTest()
    academiaTest()
    
#===============================================================================
if __name__ == "__main__":
    main()
#===============================================================================