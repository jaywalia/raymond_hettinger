from decimal import ROUND_HALF_EVEN
from random import *
from statistics import *
from collections import *

# six roulette wheel spins
# 18 reds, 18 black, 2 greens

# dummy roulette
spin = choice(['red', 'red', 'red', 'black', 'black', 'green'])
# print(spin)

# full roulette wheel
roulette = ['red']*18 + ['black']*18 + ['green']*2
# print(roulette)
spin = choice(roulette)
# print(spin)

six_spins = [choice(roulette) for _ in range(6)]
print(six_spins)

seven_spins = choices(roulette, k=7)
print(seven_spins)

# remember choices support weights, so let's use that
nine_spins = choices(['red', 'black', 'green'], [18, 18, 2], k=9)
print(nine_spins)