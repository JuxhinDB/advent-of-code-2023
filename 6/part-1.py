import sys

from operator import mul
from functools import reduce

with open(sys.argv[1]) as input_:
    lines = [x.replace('\n', '') for x in input_.readlines()]
    times = [int(t) for t in lines[0].split(':')[1].split(None)]
    distances = [int(d) for d in lines[1].split(':')[1].split(None)]
    races = zip(times, distances)

    
    winning = []
    for race in zip(times, distances):
        counter = 0
        time, record = race
        for pressed in range(0, time):
            if pressed * (time - pressed) > record:
                counter += 1
        winning.append(counter)

    print(f'Result: {reduce(mul, winning)}')

