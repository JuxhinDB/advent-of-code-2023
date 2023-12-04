import re
import sys

REGEX = r'\D+'
N_WIN = int(sys.argv[2])    # How many winning cards

# Yes I'm using global accumulator, I have places
# to be child, @ me @juxhindb
acc = 0
processed_cards = []

def process_cards(cards, original_cards):
    global acc

    for game in cards:
        (card, win, chosen) = game
        matches = len(set(win) & set(chosen))
        slice = original_cards[card : card + matches]
        process_cards(slice, original_cards)
        acc += 1

    return acc

def process_line(line):
    line = re.sub(REGEX, ',', line.replace('\n', ''))[1:].split(',')
    return (int(line[0]), 
            [int(x) for x in line[1:N_WIN + 1]],
            [int(x) for x in line[N_WIN + 1:]])

with open(sys.argv[1]) as input_:
    cards = [process_line(x) for x in input_.readlines()]
    original_cards = len(cards)
    total = process_cards(cards, cards)

    print(f'Result: {total}')

