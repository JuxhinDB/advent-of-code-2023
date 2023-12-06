import sys
import itertools

from multiprocessing import Pool


def map_fetch(map_, lookup):
    # Attempts to fetch the mapped value, if it does
    # not exist then we can simply echo back the key
    lookup = int(lookup)
    for k, v in map_.items():
        if lookup in range(k, k + v[1]):
            delta = lookup - k
            return v[0] + delta

    return lookup

def pairwise(seeds):
    seeds = iter(seeds)
    return list(zip(seeds, seeds))

with open(sys.argv[1]) as input_:
    lines = [l.replace('\n', '') for l in input_.readlines()]
    seeds = pairwise([int(l) for l in lines[0].split(' ')[1:]])

    map_alamac = {
        'seed-to-soil': {},
        'soil-to-fertilizer': {},
        'fertilizer-to-water': {},
        'water-to-light': {},
        'light-to-temperature': {},
        'temperature-to-humidity': {},
        'humidity-to-location': {} 
    }

    cur_map_str = None
    for line in lines[2:]:
        record = line.split(' ')
        if 'map' in line:
            cur_map_str = record[0]
            continue

        if all([v.isdigit() for v in record]):
            dst, src, len_ = tuple([int(v) for v in record])
            map_alamac[cur_map_str][src] = (dst, len_)

    locations = [] 
    for seed in seeds:
        print(f'trying seed: {seed}')
        # We lazy generate the range here to avoid bloating
        # memory trying to keep all the ranges ahead of time
        range_ = range(seed[0], seed[0] + seed[1])

        for seed in range_:
            cur_loc = seed
            for (k, v) in map_alamac.items():
                cur_loc = map_fetch(v, cur_loc)
            locations.append(cur_loc)
                
    print(f'Lowest location number is {min(locations)}')

