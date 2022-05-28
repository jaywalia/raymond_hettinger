# F-strings
# Counter()
# Statistics
# Random
# list concat, slice, count/index/ sorted
# lambda expressions & chained comparisons
#===============================================================================
# ways to print
x = 10

print('The answer is %d today' % 10)
print('The answer is {0} today'.format(x))
print('The answer is {x} today'.format(x=x))
print(f'The answer is {x} today')
print(f'The answer is {x**2:08d} today')
#===============================================================================
# Counter

from collections import Counter
# d = {}
# d['cats'] # << This throws key error. better use counter

d = Counter()
print(d['cats']) # << This doesn't throw the key error.

d['cats'] += 1
print(d['cats'])
print(d)

cc = Counter('red blue green red blue green red'.split())
print(cc)
print(cc.most_common(1))
print(cc.most_common(2))
# print(list(cc))
for e in cc.elements():
    print(e)
print(list(cc.values()))
print(list(cc.items()))

#===============================================================================
# Stats
from statistics import mean, median, mode, stdev

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mean(nums))
print(median(nums))
print(mode(nums))
print(stdev(nums))

#===============================================================================
# lambda expressions
sq = lambda x: x**2
print(sq(2))

cuber = lambda x: x**3
print(cuber(2))

adder = lambda x, y: x + y
print(adder(2, 3))

x = 6
if 2 < x < 8:
    print('x is between 2 and 8')

#===============================================================================
# continuous distribution

from importlib.metadata import distribution
from random import *
from statistics import *
from collections import Counter

x = random()
print(x)


u = [uniform(1000, 1100) for _ in range(1000)]
print(mean(u),stdev(u))

t = [triangular(1000, 1100) for _ in range(1000)]
print(mean(t),stdev(t))

g = [gauss(1000, 20) for _ in range(1000)]
print(mean(g),stdev(g))

e = [expovariate(10) for _ in range(1000)]
print(mean(e),stdev(e))

#===============================================================================
# disrete distribution

outcomes = ['win', 'lose', 'draw', 'double win', 'double lose', 'jackpot', 'mega jackpot']
print(choice(outcomes))
print(choice(outcomes))
print(choice(outcomes))
print(choice(outcomes))
print(choices(outcomes, k=10))
co = Counter(choices(outcomes, k=10000))
print(co)

wco = Counter(choices(outcomes,[3300, 3300, 3300, 44, 44, 11,1], k=10000))
print(wco)

# use sample for no duplicates
print(sample(outcomes, k=3))

print(sorted(sample(range(1,57), k=6)))