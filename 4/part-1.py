import re
import sys

REGEX = r'\D+'
N_WIN = int(sys.argv[2])    # How many winning cards

with open(sys.argv[1]) as input_:
    total = 0
    for line in input_.readlines():
        # Swap out the friendly line for something easier to parse
        # We swap it to CSV format and ignore the first csv.
        line = re.sub(REGEX, ',', line)[1:].split(',')
        card = line[0]
        win = line[1:N_WIN + 1]
        chosen = line[N_WIN + 1:]

        matches = set(win) & set(chosen)
        total += 2 ** (len(matches) - 1) if len(matches) > 0 else 0 

    print(f'Result: {total}')

