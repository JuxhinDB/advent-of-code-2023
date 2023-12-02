import re
import sys

from operator import mul
from functools import reduce

REGEX = r'(\d.?\sred)|(\d.?\sgreen)|(\d.?\sblue)'

def int_(v):
    return int(v.split(' ')[0])

with open(sys.argv[1]) as input_:
  total = 0

  for line in input_.readlines():
    game_id = int(line.split(' ')[1].split(':')[0]) # /Game $id: $n blue; ...
    result = [0, 0, 0]
    for res in re.findall(REGEX, line):
      match res:
        case (red, '', ''): result[0] = max(result[0], int_(red))
        case ('', green, ''): result[1] = max(result[1], int_(green)) 
        case ('', '', blue): result[2] = max(result[2], int_(blue))
        case _: sys.exit(-1)

    total += reduce(mul, result)

  print(f'Total: {total}')
