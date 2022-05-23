# https://www.youtube.com/watch?v=OSGv2VnC0go&list=PLRVdut2KPAguz3xcd22i_o_onnmDKj3MA&index=1&t=44s

#https://www.youtube.com/watch?v=OSGv2VnC0go

for i in [0,1,2,3,4,5,6]: print(i**2)

for i in range(6): print(i**2)

colors = ['red', 'green', 'blue']
balls = ['snooker', 'baseball', 'basketball']

# for c in colors: print(c)
# for c in reversed(colors): print(c)
# for c in colors[::-1]: print(c)
# for i, c in enumerate(colors): print(i, c)
for c, b in zip(colors, balls): print(c,b)

# izip in 2 is zip in 3

for c in sorted(colors): print(c)

print(sorted(colors))


#------------------------------------------------------
# ok
f = open("001.py")
blocks = []
while True:
    block = f.read(32)
    if block == '': 
        break
    blocks.append(block)

# better
from functools import partial
blocks2 = []
for block in iter(partial(f.read, 32), ''):
    blocks2.append(block)
# converting to iterator unlocks use in things like min, max, heap etc.

#------------------------------------------------------
# multiple exit points in a loop

def find(seq, tgt):
    found = False
    for i, v in enumerate(seq):
        if v == tgt:
            found = True
            break
    if not found:
        return -1
    return i

#python has a for loop with else

def find(seq, tgt):
    for i, v in enumerate(seq):
        if v == tgt: break
    else:
        return -1
    
    return i
# should have called it no break instead of else
#-------------------------------------------------------
# dictionaries

d = {'mat': 'blue', 'rachel': 'green', 'raymond': 'red'}

for k in d: print(k)

# use iteritems instead of items
# python 3 items is iteritems
# for k, v in d.iteritems(): print(f"{k}->{v}")
for k, v in d.items(): print(f"{k}->{v}")
#-------------------------------------------------------
# default dict

necklace = ['white', 'blue', 'green', 'yellow', 'white', 'green', 'blue', 'yellow']

d = {}
for beads in necklace:
    if beads not in d:
        d[beads] = 0
    d[beads] += 1
#better
for bead in necklace:
    d[bead] = d.get(bead, 0) + 1

#best :: use default dictionary
import collections
dd = collections.defaultdict(int)
for bead in necklace:
    dd[bead] += 1

#-------------------------------------------------------
# grouping with dictionaries

names = ['jay', 'john', 'jacob', 'ella', 'elizabeth', 'eliza', 'violet', 'victor']

d = {}
for n in names:
    k = n[0]
    if k not in d: d[k] = []
    d[k].append(n)

print(d)

# good
for n in names:
    k = n[0]
    d.setdefault(k, []).append(n)

# better
d = collections.defaultdict(list)
for n in names:
    k = n[0]
    d[k].append(n)

#-------------------------------------------------------
# linking dictionaries
import argparse, os
defaults = {'color':'red', 'user':'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')

namespace = parser.parse_args([])
command_line_args = {k:v for k, v in 
                    vars(namespace).items() if v}

# slow, copies data
d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)

# better : use chain map
from collections import ChainMap, deque
d = ChainMap(command_line_args, os.environ, defaults)



#-------------------------------------------------------
# clarify function calls with keyword arguments
def twitter_search(tweeter, retweets, numtweets, popular):
    pass

twitter_search('@obama', False, 20, True)
twitter_search(tweeter='@obama', retweets=False, numtweets=20, popular=True)

#-------------------------------------------------------
# clarify multiple return values with named tuples
from collections import namedtuple

# print(doctest.testmod())
TestResults = namedtuple('TestResults', ['failed', 'attempted'])

#-------------------------------------------------------
# unpacking sequence

p = 'Raymond', 'Hettinger', 'rh@python.org'
print(p)
# ok
fname = p[0]
lname = p[1]

#better
fname, lname = p[0], p[1]
print(fname,lname)
#best
fname, lname, email = p
print(fname,lname, email)

#-------------------------------------------------------
# simultaneous update state variables
# use tuple packing and unpacking

def fib(n):
    x, y = 0, 1
    for i in range(n):
        t = y
        y = x + y
        x = t
    return x

def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x+y
    return x

print(fib(7))
print(fibonacci(7))

#-------------------------------------------------------
# concatenating strings
# Quadratic behavior : don't do following

s = names[0]
for n in names[1:]:
    s += ', ' + n
print(s)

# Better
# use join
names_csv = ', '. join(names)
print(names_csv)

#-------------------------------------------------------
# updating sequences

# DON"T DO FOLLOWING
# Following make it slow
del names[0]
names.pop(0)
names.insert(0, 'mark')

# INSTEAD use deque
from collections import deque
dq_names = deque(names)
del dq_names[0]
dq_names.popleft()
dq_names.appendleft('mark')
